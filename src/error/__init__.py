class AppException(Exception):
    def __init__(self, message: str, error_code: int = 400) -> None:
        super().__init__(message)
        self.__error_code = error_code

    @property
    def error_code(self) -> int:
        return self.__error_code
