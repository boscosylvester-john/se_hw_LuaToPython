import sys
import random
from .Utils import *

class Num:
    def __init__(self, c = 0, s = ""):
        self.n = 0
        self.at = c
        self.name = s
        self._has = {}
        self.lo = sys.maxsize
        self.hi = -sys.maxsize
        self.isSorted = True
        if len(s) == 0:
            self.w = 1
        else:
            self.w = -1 if s[-1] == "-" else 1
    
    def nums(self):
        if not self.isSorted:
            sorted(self._has)
            self.isSorted = True
        return self._has
    
    # this function needs to be updated after 'the' is implemented
    def add(self, v):
        if v != "?":
            self.n = self.n + 1
            self.lo = min(v, self.lo)
            self.hi = max(v, self.hi)
        if len(self._has) < the.nums:
            pos = 1 + len(self._has)
        elif random.random() < the.nums / self.n:
            pos = random.random(len(self._has))
        if pos:
            self.isSorted = False
        else:
            self._has[pos] = int(v)

    def div(self):
        a = self.nums
        return (per(a, 0.9) - per(a, 0.1)) / 2.58

    def mid(self):
        return per(self.nums(), 0.5)

