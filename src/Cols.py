import re

from src.Num import Num
from src.Sym import Sym

class Cols:
    def __init__(self, names):
        self.names = names
        self.all = []
        self.klass = None
        self.x = []
        self.y = []
        for c,s in names.items():
            col = None
            if re.search("^[A-Z]", s):
                col = Num(c, s)
            else:
                col = Sym(c, s)
            self.all.append(col)
            if s[-1] != ":":
                if re.search("[!+-]", s):
                    self.y.append(col)
                else:
                    self.x.append(col)
                if s[-1] == "!":
                    self.klass = col
            