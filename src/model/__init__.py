__all__ = ["data.main", "src.main", "training.main"]  # File names to export
# To add backwards compatbility when importing from other files, simply add:
# from .fileName import functionName
from .src.main import *
from .training.main import *
from .data.main import *


def runModel():
    test()
