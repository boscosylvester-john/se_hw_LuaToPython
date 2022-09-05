import sys
import random
from Utils import *

class Sym:
    def __init__(self, c = 0, s = ""):
        self.n = 0
        self.at = c
        self.name = s
        self._has = {}
    
    def add(self, v):
        if v != "?":
            self.n = self.n + 1
            self._has[v] =  1 + (self._has[v])
           