from HELPER import *
from DDICT import *
while True:
#def formatDict(dict):
 mt=[];mtNm=[]
 for i in Dict:
  mt.append(i)
  mtNm.append(Dict[i]["infos"]["name"])
  print(mt,mtNm)
  #return mt,mtNm
 
 print(formatDict(Dict))
 input()