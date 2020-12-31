# 32*11
from HELPER import *
from DDICT import Dict as d
while True:
 cl();sbj=[];name=[]
 for isb in d:
  sbj.append(isb)
  for inm in d[isb]["dict"]:
   name.append(inm)
   lprint(d[isb]["dict"][inm]["name"]+":")
   lprint(d[isb]["dict"][inm]["def"])
   lprint("--------------------")
 input()