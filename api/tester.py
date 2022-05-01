from plugins.reflection.module import Module
from plugins.reflection.method import MethodInfo
from sqlalchemy.sql.schema import Column
from db.models import DB
from db.utils.io import IOHelper
from exceptions.invalid_token import InvalidTokenException
from api.auth import AuthManager
from flask_cors.decorator import cross_origin
from flask.blueprints import Blueprint
from flask.globals import request
from api import RouteAPI
from db.models.user import UserModel


class TesterAPI(RouteAPI):
    __router = Blueprint(__name__, __name__)

    @staticmethod
    def resister_route():
        return TesterAPI.__router

    @__router.route("/test", methods=['GET'])
    def test():
        model = UserModel("Hello", "新しいユーザー")
        io = IOHelper(UserModel)
        io.write(model)
        return "Sucess"

    @__router.route("/auth/test", methods=['GET'])
    @cross_origin(supports_credentials=True)
    def auth_tester():
        certificate = AuthManager.get_certificate(request)
        if certificate is None:
            return InvalidTokenException.message()
        else:
            if certificate.is_valid_user is False:
                return InvalidTokenException.message()
            else:
                return certificate.user_info.user.displayName
