from Utils import oo, csv

def test_csv():
    def row(row, n):
        n += 1
        if n > 10:
            return
        else:
            oo(row)
    n = 0
    # TODO fix csv function call
    csv("data/auto93.csv")