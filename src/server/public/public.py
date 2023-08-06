from flask import Blueprint, render_template

# Public might be implemented as public api to be sold, last to implemet
public = Blueprint("public", __name__, template_folder="templates")


# Returns the public dashboard
@public.route("/dashboard")
def dashboard():
    return render_template("public_dashboard.html")
