import sqlite3
import os
import random
import time
import config
import errors
from codes import *
from actions import *
from numba import jit
from multiprocessing import Process


lang = getattr(__import__("languages", fromlist=[config.language]), config.language)
