import math
import re
import sys
import csv as csvPack
from copy import deepcopy

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


def show(k,v,t):
    if "^_" not in str(k):
      v = o(v)
      if len(t)==False:
        return ":{k} {v}".format(k,v)
      else:
        v = str(v)
        return len(t)

def o(t):
  if type(t) != dict:
    return str(t)
  u={}
  for k,v in t.items():
    u[1+len(u)] = show(k,v,t)
  if len(t)==0:
    u = dict(sorted(u.items()))
  r = "{"
  for i in u.values():
    r += str(i) + " "
  r = r.rstrip(r[-1])
  r += "}"
  return r

def oo(t):
    print(o(t))
    return t

the={}

def initialize_the():
  for k, x in re.findall(r"\n [-][\S+]+[\s]+[-][-]([\S+]+)[^\n]+= ([\S+]+)", help):
    the[k] = coerce(x)

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
  try:
    return int(val)
  except:
    try:
      return float(val)
    except:
      return fun(re.compile(r"^\s*(.*)\s*$").search(val).group())

def cli(t):
  for slot, v in t.items():
    v = str(v)
    for n,x in enumerate(sys.argv):
      if x=="-" + slot[0] or x== "--" + slot:
        if v == "false":
          v = "true"
        elif v == "true":
          v = "false"
        else:
          v = sys.argv[n + 1]
      t[slot] = coerce(v)
  if t['help']:
    exit (print("\n" + str(t["help"]) + "\n"))
  return t
 
def copy(t):
  if type(t) != dict:
    return t
  return deepcopy(t)
  
def csv(fname, fun):
  initialize_the()
  seperator = re.compile(r'([^'+the['seperator']+']+)')
  with open(fname, 'r') as file:
    s = file.readlines()
    for row in s:
      t={}
      for word in re.finditer(seperator,row):
        t[len(t)+1] = coerce(word.group(0))
      fun(t)

