from flask import Blueprint
import src.model

api = Blueprint("api", __name__)


# Returns a 200 ok response if the app is running correctly
@api.route("/status", methods=["GET"])
def status():
    return 200
