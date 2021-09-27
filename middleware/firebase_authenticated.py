from functools import wraps
from firebase_admin import auth
import jwt
from sanic import text


def check_token(request):
    if not request.token:
        return False

    try:
        result = auth.verify_id_token(request.token)
        print(result)
    except jwt.exceptions.InvalidTokenError:
        return False
    else:
        return True


def firebase_authenticated(wrapped):
    def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            is_authenticated = check_token(request)

            if is_authenticated:
                response = await f(request, *args, **kwargs)
                return response
            else:
                return text("You are unauthorized.", 401)

        return decorated_function

    return decorator(wrapped)
