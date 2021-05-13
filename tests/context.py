"""TEMP."""

import os
import sys
import pathlib
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pyisc

data_folder = pathlib.Path(__file__).parent.parent.joinpath('data')
