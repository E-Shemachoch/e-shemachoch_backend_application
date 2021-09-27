
access_control = {
    '/products': {
        'CONSUMER': ['GET'],
        'ADMIN': ['GET', 'POST', 'DELETE', 'PUT'],
    },
    '/products/images': {
        'CONSUMER': ['GET'],
        'ADMIN': ['GET', 'POST', 'DELETE', 'PUT'],
    },
    '/notices': {
        'CONSUMER': ['GET'],
        'ADMIN': ['GET', 'POST', 'DELETE', 'PUT'],
    },
    '/consumers': {
        'ADMIN': ['GET', 'POST', 'DELETE', 'PUT'],
    },
    '/consumers/images': {
        'CONSUMER': ['GET'],
        'ADMIN': ['GET', 'POST', 'DELETE', 'PUT'],
    },
    '/orders': {
        'CONSUMER': ['POST'],
        'ADMIN': ['GET'],
    },
    '/orders/consumers': {
        'CONSUMER': ['GET'],
    },
    '/reports': {
        'ADMIN': ['GET'],
    },
}


def check_access(url: str, method: str, role: str):
    stripped_url = str.join('/', url.split('/')[:-1])
    if url in access_control:
        route = access_control[url]
        if role in route and method in route[role]:
            return True
    elif stripped_url in access_control:
        route = access_control[stripped_url]
        if role in route and method in route[role]:
            return True
    else:
        return False
