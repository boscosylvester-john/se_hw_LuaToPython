from tokenize import String
from Utils import * 
from Cols import *
from Row import *

class Data:
    def __init__(self,src):
        self.cols  = None
        self.rows = {}
        if type(src) == str:
            csv(src,self.add(row))
        else:
            for row in src or {}:
                self.add(row)

    def add(self,xs):
        if self.cols == None:
            self.cols = Cols(xs)
        else:
            row = push(self.rows, xs.cells and xs or Row(xs))
            for todo in list(self.cols.x,self.cols.y) :
                for col in todo:
                    col.add(row.cells(col.at))
                    
    def stats(self, places,showCols,fun):
        if showCols is None:
            showCols = self.cols.y
        if fun is None:
            fun = "mid"
        t={}
        for col in showCols:
            v=fun(col)
            v = type(v) == float and rnd(v,places) or v 
            t[col.name] = v
        return t