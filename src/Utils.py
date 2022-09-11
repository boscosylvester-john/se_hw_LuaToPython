import math
import regex as re

help = """CSV : summarized csv file
(c) 2022 Tim Menzies <timm@ieee.org> BSD-2 license

USAGE: lua seen.lua [OPTIONS]

OPTIONS:
 -e  --eg        start-up example                      = nothing
 -d  --dump      on test failure, exit with stack dump = false
 -f  --file      file with csv data                    = ../data/auto93.csv
 -h  --help      show help                             = false
 -n  --nums      number of nums to keep                = 512
 -s  --seed      random number seed                    = 10019
 -S  --seperator feild seperator                       = ,"""

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

def show(k,v,t):
    if "^_" not in str(k):
      v = o(v)
      if len(t)==False:
        return ":{k} {v}".format(k,v)
      else:
        v = str(v)
        return len(t)

def o(t):
  if isinstance(t,dict):
    return str(t)
  u={}
  for k,v in t.items():
    u[1+len(u)] = show(k,v,t)
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

def initialize_the():
    the = {}
    reg = re.compile(r"-[\S+]\s+--[\S+]+\s+[\S+]+\s+=\s[\S+]+", re.IGNORECASE)
    text = re.findall(reg,help)
    for i in text:
      a = re.compile(r"-[\S+]\s+--[\S+]+\s+[\S+]+\s+", re.IGNORECASE)
      b = re.compile(r"=\s[\S+]+", re.IGNORECASE)
      c = re.search(b,i).group()[2:]
      the[re.search(a,i).group()] = coerce(c)
    return the 

def the():
    oo(initialize_the())
    return True
