from Utils import oo, csv
import unittest

class TestingCSV(unittest.TestCase):
    def test_csv(self):
        def row(t, n):
            n += 1
            if n > 10:
                return  
            else:
                oo(t)
        n = 0
        csv("../data/testdata.txt", lambda t, n=n: row(t, n))

if __name__ == "__main__":
    unittest.main()