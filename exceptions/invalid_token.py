from plugins.reflection.decorators import static


class InvalidTokenException(BaseException):
    @staticmethod
    def message():
        return "0: unexpected token."
