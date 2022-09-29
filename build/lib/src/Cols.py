import re

from Num import Num
from Sym import Sym

class Cols:
    def __init__(self, names):
        self.names = names
        self.all = []
        self.klass = None
        self.x = []
        self.y = []
        for c,s in names.items():
            col = None
            if s[0].isupper():
                col = Num(c, s)
            else:
                col = Sym(c, s)
            self.all.append(col)
            if s[-1] != ":":
                if s[-1] in ['+', '-', '!']:
                    self.y.append(col)
                    # print("added in Y")
                else:
                    self.x.append(col)
                    # print("added in X")
                if s[-1] == "!":
                    self.klass = col
            