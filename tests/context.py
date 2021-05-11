"""TEMP."""

import os
import sys
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pathlib
import pyisc

data_folder = pathlib.Path(__file__).parent.parent.joinpath('data')
