# This is the server exported file, functions and variables defined here are
# the "external" that the entire app can and will use

from flask import Flask, request
from .api.api import api
from .admin.admin import admin
from .public.public import public

app = Flask("name")
app.register_blueprint(public)
app.register_blueprint(api, url_prefix="/api")
app.register_blueprint(admin, url_prefix="/admin")


def init_server():
    print("\nServer Initialization\n")
    app.run(host="localhost", port=8000, debug=True)
