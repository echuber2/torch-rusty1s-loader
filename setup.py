
# make sure torch is installed
import os
os.system('python3 -m pip install wheel')

from setuptools import setup
setup(
    name='torch-rusty1s-loader',
    version='0.1',
    extras_require={
        "findblas": ["findblas"],
        "torch-bincount": ["torch-bincount"],
        "torch-cluster": ["torch-cluster"],
        "torch-geometric": ["torch-geometric"],
        "torch-scatter": ["torch-scatter"],
        "torch-sparse": ["torch-sparse"],
        "torch-spline-conv": ["torch-spline"],
        "torch-unique": ["torch-unique"]
    }
)
