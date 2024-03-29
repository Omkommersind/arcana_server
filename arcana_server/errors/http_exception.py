from django.utils.encoding import force_text
from rest_framework.exceptions import APIException

from arcana_server.errors.errors import Errors


class HttpException(APIException):
    default_detail = Errors.INTERNAL_SERVER_ERROR.name
    default_code = Errors.INTERNAL_SERVER_ERROR

    def __init__(self, detail=None, status_code=None):
        self.status_code = status_code
        if detail is None:
            detail = force_text(self.default_detail)
        if status_code is None:
            status_code = self.default_code
        super(HttpException, self).__init__(detail, status_code)
