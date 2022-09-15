from src import Sym 
from src import Utils as utils
from src import Data as data

def test_data():
  d = data.Data("https://raw.githubusercontent.com/timm/lua/main/data/auto93.csv")
  for _,col in d.cols.y:
    utils.oo(col)
    print("ded")
  return True
