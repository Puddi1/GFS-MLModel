# This is the server exported file, functions and variables defined here are
# the "external" that the entire app can and will use
import src.huggingface as hf
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
    print(hf.DownloadFromHfHub("", ""))

    if st.DEVELOPMENT == "true":
        print("\nServer Initialization in Development Environment\n")
        app.run(host=st.HOST, port=st.PORT, debug=True)
        return

    print("\nServer Initialization in Production Environment\n")
    serve(app, host=st.HOST, port=st.PORT)
