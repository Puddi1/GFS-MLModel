from flask import Blueprint
import model

api = Blueprint("api", __name__)


@api.route("/status", methods=["GET"])
def status():
    return
