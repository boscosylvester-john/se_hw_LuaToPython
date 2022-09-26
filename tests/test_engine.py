from cgi import test
import random
import Utils as utils
import test_cases

class TestEngine:
    def __init__(self):
        self.fails = 0
        self.eg = {}
    
    def runs(self, k):
        if k not in self.eg:
            return
        random.seed(utils.the["seed"])
        old = {k:v for (k,v) in utils.the.items()}
        if utils.the["dump"]:
            status, out = True, self.eg[k]()
        else:
            try:
                out = self.eg[k]()
                status = True
            except:
                out = False
                status = False
        
        for k,v in old.items():
            utils.the[k] = v
        if status:
            msg = "PASS" if out else "FAIL"
        else:
            msg = "CRASH"
        print("!!!!!!", msg, k, status)
        return out

    def BAD(self):
        print(self.dont.have.this.field)

    def LIST(self):
        tests = test_cases.TestCases()
        t = {"ALL": self.ALL, "the": tests.test_the, "sym": tests.test_sym, "num": tests.test_num, "bignum": tests.test_bigNum, "data" : tests.test_data, "stats": tests.test_stats, "csv": tests.test_csv}
        sortedTests = sorted(t)
        return sortedTests

    def LS(self):
        print("\nExamples lua csv -e ...")
        for i, k in self.LIST().items():
            print(i)
        return True
    
    def ALL(self):
        for i, k in self.LIST().items():
            if i != "ALL":
                print(i)
                print("\n-----------------------------------")
                if not self.runs(k):
                    self.fails += 1
        return True