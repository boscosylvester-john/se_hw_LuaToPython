from src import Num 
from src import Utils as utils

def test_num():
    num = Num.Num()
    for i in range(1,101):
        num.add(i)
    mid, div = num.mid(), num.div()
    print(mid ,div)
    return 50<= mid and mid<= 52 and 30.5 <div and div<32

def test_bigNum():
    num = Num.Num()
    utils.the['nums'] = 32
    for i in range(1,1001):
        num.add(i)
    utils.oo(num.nums())
    return 32==len(num._has)