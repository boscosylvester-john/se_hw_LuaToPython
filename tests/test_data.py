import Sym as sym
import Utils as utils
import Data as data
import unittest

class TestingData(unittest.TestCase):
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
    print('ymid=', d.stats(3, d.cols.y, "div"))
    return True

if __name__ == "__main__":
    unittest.main()

    