import random
import Utils as utils

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