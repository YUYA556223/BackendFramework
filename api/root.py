from flask.blueprints import Blueprint
from api import RouteAPI


class Root(RouteAPI):
    __router = Blueprint(__name__, __name__)

    @staticmethod
    def resister_route():
        return Root.__router

    @__router.route("/", methods=['GET'])
    def entry_point():
        return "Connection sucess."
