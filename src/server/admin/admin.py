from flask import Blueprint, render_template

admin = Blueprint("admin", __name__, template_folder="templates")


# Returns the admin dashboard
@admin.route("/", methods=["GET"])
def index():
    return render_template("dashboard.html")
