from db.handlers.user import UserHandler
from plugins.reflection.activator import Activator
from plugins.reflection.bindingflags import BindingFlags
from plugins.reflection.type import typeof
from flask.blueprints import Blueprint
from api import RouteAPI


class UserAPI(RouteAPI):
    __router = Blueprint(__name__, __name__)

    @staticmethod
    def resister_route():
        return UserAPI.__router

    @staticmethod
    def test2():
        return "Hello"

    @__router.route("/user")
    def TestRoute():
        UserHandler.test()
        return "DONE"
