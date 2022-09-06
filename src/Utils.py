import math
import regex as re

def per(t, p = 0.5):
    p = math.floor((p * len(t)) + 0.5)
    ind = max(1, min(len(t), p))
    return t[ind]

def logarithm(p):
    return p*math.log2(p)

def fun(s1):
    if s1=="true":
        return True 
    if s1=="false":
        return False
    return s1 

def coerce(s):
    try:
        return int(s)
    except:
        return re.search(s,"^%s*(.-)%s*$")

def show(k,v):
    if "^_" not in str(k):
      v = o(v)
      if len(t)==False:
        return ":{k} {v}".format(k,v)
      else:
        v = str(v)
        return len(t)

def o(t,u):
  if isinstance(t,dict):
    return str(t)
  u={}
  for k,v in pairs(t):
    u[1+len(u)] = show(k,v)
  if len(t)==0:
    q = sorted(u)
  r = "{"
  for i in q.values():
    r += str(i) + " "
  r = r.rstrip(r[-1])
  r += "}"
  return r

def oo(t):
    print(o(t))
    return t

def the():
    oo(the)
    return True
