import Utils as utils
import Data as data
import Sym, Num

class TestCases:
    def test_the(self):
        utils.oo(utils.initialize_the())
        return True

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

    def test_num(self):
        num = Num.Num()
        utils.the['nums'] = 512
        for i in range(1,101):
            num.add(i)
        mid, div = num.mid(), num.div()
        self.assertTrue(mid >= 50 and mid <= 52 and div > 30.5 and div < 32)

    def test_bigNum(self):
        num = Num.Num()
        utils.the['nums'] = 32
        for i in range(1,1001):
            num.add(i)
        currentNums = num.nums()
        dictNums = {index:currentNums[index] for index in range(len(currentNums))}
        utils.oo(dictNums)
        self.assertEqual(32, len(num._has))

    def test_data(self):
        d = data.Data("data\\testdata.txt")
        for col in d.cols.y:
            utils.oo(col)
        return True

    def test_stats(self):
        d = data.Data("data\\testdata.txt")
        print('xmid=', d.stats(2, d.cols.x, "mid"))
        print('xdiv=', d.stats(3, d.cols.x, "div"))
        print('ymid=', d.stats(2, d.cols.y, "mid"))
        print('ydiv=', d.stats(3, d.cols.y, "div"))
        return True

    def test_csv(self):
        def row(t, n):
            n += 1
            if n > 10:
                return  
            else:
                utils.oo(t)
        n = 0
        utils.csv("data\\testdata.txt", lambda t, n=n: row(t, n))