import sys
import random
from .Utils import *

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
    
    def mid(self):
      mode = most = -1
      for k, v in self._has.items():
        if v > most:
          mode = k
          most = v
      return mode
    
    def div(self):
      e = 0
      for k, v in self._has.items():
        if v > 0:
          e = e - logarithm(v/self.n)
      return e
