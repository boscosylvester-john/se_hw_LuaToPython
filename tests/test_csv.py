from Utils import oo, csv

def test_csv():
    def row(t, n):
        n += 1
        if n > 10:
            return  
        else:
            oo(t)
    n = 0
    csv("data/auto93.csv", lambda t, n=n: row(t, n))