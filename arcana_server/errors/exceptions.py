class BaseServerException(Exception):
    def __init__(self, detail, status_code, message):
        super().__init__(message)
        self.detail = detail
        self.status_code = status_code


class EntityDoesNotExistException(BaseServerException):
    def __init__(self):
        super().__init__(detail='Entity not found', status_code=404, message='Entity not found')


class InternalIOException(BaseServerException):
    def __init__(self):
        super().__init__(detail='In out internal server exception', status_code=404,
                         message='In out internal server exception')


class WrongConsultationStatusException(BaseServerException):
    def __init__(self):
        super().__init__(detail='Wrong consultation status for the operation', status_code=404,
                         message='Wrong consultation status for the operation')
