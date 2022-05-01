from db.models import DB
from api.auth.certificate import Certificate
from db.models.user import UserModel
from db.utils.io import IOHelper


class UserHandler:
    @staticmethod
    def test():
        print("This is user handler class")
