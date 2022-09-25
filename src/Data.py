from tokenize import String
from Utils import * 
from Cols import *
from Row import *

class Data:
    def __init__(self,src):
        self.cols  = None
        self.rows = {}
        if type(src) == str:
            csv(src, lambda row: self.add(row))
        else:
            for row in src or {}:
                self.add(row)

    def add(self,xs):
        if self.cols == None:
            self.cols = Cols(xs)
        else:
            try:
                row = push(self.rows, xs.cells)
            except:                
                row = push(self.rows, Row(xs).cells)
            for col in self.cols.x:
                col.add(row[col.at])
            for col in self.cols.y:
                col.add(row[col.at])
                    
    def stats(self, places,showCols,fun):
        if showCols is None:
            showCols = self.cols.y
        if fun is None:
            fun = "mid"
        t={}
        for col in showCols:
            if fun == "mid":
                v = col.mid()
            else:
                v=col.div()
            v = type(v) == float and rnd(v,places) or v 
            t[col.name] = v
        return t
