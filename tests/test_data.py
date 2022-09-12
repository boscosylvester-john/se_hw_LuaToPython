from src import Sym 
from src import Utils as utils
from src import Data
import pytest

def test_data():
  d = Data.Data("https://raw.githubusercontent.com/timm/lua/main/data/auto93.csv")
  for _,col in d[y].items():
    utils.oo(col)
  return true
