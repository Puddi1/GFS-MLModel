from flask import Blueprint

public = Blueprint("public", __name__, template_folder="templates")

# Public might be implemented as public api to be sold, last to implemet


#
@public.route("/")
def index():
    return "Index public route"
