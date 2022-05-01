from flask.blueprints import Blueprint
from api import RouteAPI


class StatusAPI(RouteAPI):
    __router = Blueprint(__name__, __name__)

    @staticmethod
    def resister_route():
        return StatusAPI.__router

    @__router.route("/status", methods=['GET'])
    def get_server_status():
        return "status: "
