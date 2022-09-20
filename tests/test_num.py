import Num 
import Utils as utils
import unittest

class TestingNum(unittest.TestCase):
    def test_num(self):
        num = Num.Num()
        utils.the['nums'] = 512
        for i in range(1,101):
            num.add(i)
        print("check: ", num.nums())
        mid, div = num.mid(), num.div()
        print("checking:", mid)
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

if __name__ == "__main__":
    unittest.main()