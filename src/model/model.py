# This is the model exported file, functions and variables defined here are
# the "external" that the entire app can and will use

from .train.train import *
from .data.data import *

import pandas as pd
from jax import random


def valueString():
    b = train()
    test()

    df = pd.DataFrame(
        {
            "Name": [
                "Braund, Mr. Owen Harris",
                "Allen, Mr. William Henry",
                "Bonnell, Miss. Elizabeth",
            ],
            "Age": [22, 35, 58],
            "Sex": ["male", "male", "female"],
        }
    )
    print(df)

    key = random.PRNGKey(0)
    x = random.normal(key, (10,))
    print(x)

    print("Model Ready")
    return "Response from module: " + b + " With data type: "
