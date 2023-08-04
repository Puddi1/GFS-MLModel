# This is the model exported file, functions and variables defined here are
# the "external" that the entire app can and will use

from .train.train import *
from .data.data import *


def valueString():
    b = train()
    test()

    print("Model2 Ready")
    return "Response from module: " + b + " With data type: "
