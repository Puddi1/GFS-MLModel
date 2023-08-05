# This is the server exported file, functions and variables defined here are
# the "external" that the entire app can and will use

import settings as st
from waitress import serve
from flask import Flask
from .api.api import api
from .admin.admin import admin
from .public.public import public

app = Flask("GFS-MLModel")
app.register_blueprint(public)
app.register_blueprint(api, url_prefix="/api")
app.register_blueprint(admin, url_prefix="/admin")


def init_server():

    if st.DEVELOPMENT == "true":
        print("\nServer Initialization in Development Environment\n")
        app.run(host=st.HOST, port=st.PORT, debug=False)
        return

    serve(app, host=st.HOST, port=st.PORT)
