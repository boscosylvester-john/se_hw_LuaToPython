from src import Sym 
from src import Utils as utils
import pytest

sym=Sym.Sym(1,"name")

print(sym._has)

def test_the():
    utils.oo(utils.initialize_the())
    return True

def test_sym():
    for v in ["a","a","a","a","b","b","c"]:
        sym.add(v)
    mode = sym.mid()
    entropy = sym.div()
    entropy = (1000*entropy)//1/1000
    t = {}
    t["mid"] = mode
    t["div"] = entropy
    utils.oo(t)
    assert mode == "a" and 1.37<= entropy and entropy<= 1.38
