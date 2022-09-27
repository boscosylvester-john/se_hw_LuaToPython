import sys 
from os import path
from pathlib import Path

testPath = str(Path(__file__).parent.absolute())
codePath = str(Path(Path(__file__).parent.parent/"src").absolute());

sys.path.append(testPath)
sys.path.append(codePath)

import Utils as utils
import random
# from src import Utils as utils
import test_cases

class TestEngine:
    def __init__(self):
        self.fails = 0
        # self.eg = {}
    
    def runs(self, funcName, func):
        # if k not in self.eg:
        #     return
        if "seed" in utils.the.keys():
            random.seed(utils.the["seed"])
        old = {k:v for (k,v) in utils.the.items()}
        if "dump" in utils.the.keys() and utils.the["dump"]:
            status, out = True, func()
        else:
            try:
                out = func()
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
        print("!!!!!!", msg, funcName, status)
        return out

    def BAD(self):
        print(self.dont.have.this.field)

    def LIST(self):
        tests = test_cases.TestCases()
        t = {"ALL": self.ALL, "the": tests.test_the, "sym": tests.test_sym, "num": tests.test_num, "bignum": tests.test_bigNum, "data" : tests.test_data, "stats": tests.test_stats, "csv": tests.test_csv}
        sortedDict = dict(sorted(t.items(), key = lambda x : x[0]))
        return sortedDict

    def LS(self):
        print("\nExamples lua csv -e ...")
        for i, k in self.LIST().items():
            print(i)
        return True
    
    def ALL(self): 
        total = 0 
        for k, v in self.LIST().items():
            if k != "ALL":
            # if k == "bignum":
                total += 1
                print(k)
                print("-----------------------------------")
                if not self.runs(k, v):
                    self.fails += 1
        print(total-self.fails, "/", total, " test cases passed!")
        return True