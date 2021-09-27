from functools import wraps
from worker.access_control import check_access
from sanic.response import text
import jwt


def check_authorization(request):
    payload = jwt.decode(
        request.token, request.app.config.JWT_KEY, algorithms=["HS256"]
    )
    return check_access(request.path, request.method, payload['role'])


def authorized(wrapped):
    def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):

            is_authorized = check_authorization(request)

            if is_authorized:
                response = await f(request, *args, **kwargs)
                return response
            else:
                return text("Forbidden access.", 403)
        return decorated_function
    return decorator(wrapped)
