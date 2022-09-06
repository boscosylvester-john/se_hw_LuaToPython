import math

def per(t, p = 0.5):
    p = math.floor((p * len(t)) + 0.5)
    ind = max(1, min(len(t), p))
    return t[ind]

def logarithm(p):
    return p*math.log2(p)