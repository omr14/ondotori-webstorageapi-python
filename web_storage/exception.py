class HTTPException(Exception):
    def __init__(self, response, *args, **kwargs):
        try:
            error = response.json()['error']
            message = '{} {}'.format(error['code'], error['message'])
        except Exception:
            if hasattr(response, 'status_code') and response.status_code == 401:
                message = response.content.decode('utf8')
            else:
                message = response
        super(HTTPException, self).__init__(message, *args, **kwargs)


class HTTPBadRequest(HTTPException):
    """ Greater than 400 """
    pass


class HTTPUnauthorized(HTTPException):
    """ 401 """
    pass


class HTTPForbidden(HTTPException):
    """ 403 """
    pass


class HTTPUnsupportedMediaType(HTTPException):
    """ 415 """
    pass


class HTTPTooManyRequests(HTTPException):
    """ 429 """
    pass


class HTTPServerError(HTTPException):
    """ Greater than 500 """
    pass


class HTTPServiceUnavailable(HTTPException):
    """ 503 """
    pass


def detect_exception(response):
    if response.status_code == 401:
        raise HTTPUnauthorized(response)
    elif response.status_code == 403:
        raise HTTPForbidden(response)
    elif response.status_code == 404:
        raise HTTPNotFound(response)
    elif response.status_code == 415:
        raise HTTPUnsupportedMediaType(response)
    elif response.status_code == 429:
        exc = HTTPTooManyRequests(response)
        exc.retry_after_secs = int(response.headers['X-RateLimit-Remaining'])
        raise exc
    elif response.status_code == 503:
        raise HTTPServiceUnavailable(response)
    elif response.status_code >= 500:
        raise HTTPServerError(response)
    elif response.status_code >= 400:
        raise HTTPBadRequest(response)
