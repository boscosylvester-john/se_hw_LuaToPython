import Sym 
import Utils as utils
import unittest

class TestingSym(unittest.TestCase):

    def test_sym(self):
        sym = Sym.Sym(1, "name")
        for v in ["a","a","a","a","b","b","c"]:
            sym.add(v)
        mode = sym.mid()
        entropy = sym.div()
        entropy = (1000*entropy)//1/1000
        t = {}
        t["mid"] = mode
        t["div"] = entropy
        utils.oo(t)
        self.assertTrue(mode == "a" and entropy >= 1.37 and entropy <= 1.38)

if __name__ == "__main__":
    unittest.main()
