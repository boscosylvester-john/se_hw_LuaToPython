import math
import re

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
    print("value of p is: ")
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

the={"nums":512}
def initialize_the():
    reg = re.compile(r"-[\S+]\s+--[\S+]+\s+[\S+]+\s+=\s[\S+]+", re.IGNORECASE)
    text = re.findall(reg,help)
    for i in text:
      a = re.compile(r"-[\S+]\s+--[\S+]+\s+[\S+]+\s+", re.IGNORECASE)
      b = re.compile(r"=\s[\S+]+", re.IGNORECASE)
      c = re.search(b,i).group()[2:]
      the[re.search(a,i).group()] = coerce(c)
    return the 

def rnd(x, places):
  if places is None:
    mult = math.pow(10,2)
  else:
    mult = math.pow(10,places)
  return (math.floor(x*mult +0.5)/mult)

def push(t,x):
  t[len(t)+1] = x
  return x

def coerce(val):
  if type(val) == int:
    return int(val)
  else:
    if val == 'true': return True
    if val == 'false': return False
    else:
      return re.compile(r"^\s*(.*)\s*$").search(val).group()


def csv(fname, fun):
  separator = the['separator']
  rows = []
  with open(fname, 'r', encoding='utf-8') as file:
    s = list(csv.reader(file))
  for i in range(len(s)):
    t=[]
    for word in s[i].split(separator):
      t.append(coerce(word))
    fun(t)
