import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

DEVELOPMENT = os.environ.get("DEVELOPMENT")
PORT = os.environ.get("PORT")
HOST = os.environ.get("HOST")
