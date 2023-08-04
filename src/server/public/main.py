from flask import Blueprint


def public():
    bl = Blueprint("public", __name__, template_folder="templates")
    print(bl)
