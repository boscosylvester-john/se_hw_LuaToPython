import os, sys
current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.abspath(os.path.join(current_dir, "../src"))
sys.path.append(source_dir)

import test_csv, test_data, test_num, test_sym
import unittest

class LuaTesting(unittest.TestCase):
    def test_data(self):
        test_data.test_data()
    
    def test_num(self):
        test_num.test_num()
    
    def test_bignum(self):
        test_num.test_bigNum()
    
    def test_sym(self):
        test_sym.test_sym()
    
    def test_csv(self):
        test_csv.test_csv()

    def test_the(self):
        test_sym.test_the()


if __name__ == '__main__':
    unittest.main()