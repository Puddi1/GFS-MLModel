from flask import Flask
from .admin.main import admin
from .public.main import public


def init_server():
    admin()
    public()
