import Sym 
import Utils as utils
import Data as data
import unittest

class TestingData(unittest.TestCase):
  def test_data(self):
    d = data.Data("https://raw.githubusercontent.com/timm/lua/main/data/auto93.csv")
    for _,col in d.cols.y:
      utils.oo(col)
    return True

if __name__ == "__main__":
    unittest.main()