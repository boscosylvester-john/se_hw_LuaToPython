import sys
import random
from .Utils import *

class Row:
    def __init__(self, t):
        self.cells = t
        self.cooked = t.copy()
        self.isEvaled = False
