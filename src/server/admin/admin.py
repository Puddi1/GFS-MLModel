from flask import Blueprint, render_template

admin = Blueprint("admin", __name__, template_folder="templates")


# Returns the admin dashboard
@admin.route("/dashboard", methods=["GET"])
def dashboard():
    # Check if is Admin
    return render_template("admin_dashboard.html")
