from enum import IntEnum


def choices(em):
    return [(e.value, e.name) for e in em]


class Errors(IntEnum):
    NOT_AUTHORIZED = 401
    BAD_REQUEST = 400
    ACCESS_DENIED = 403
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500
