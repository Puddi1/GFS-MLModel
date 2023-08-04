from flask import Blueprint


def admin():
    bl = Blueprint("admin", __name__, template_folder="templates")
    print(bl)
