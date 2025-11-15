import All
import csv
import os
from pathlib import Path
import shutil
try:
  shutil.rmtree("CollectedData")
except:
  pass
with open("DATA.txt", "r") as f:
  DAT = f.read()
  DATA = eval(DAT)
if DATA == None:
  DATA = All.MainInputNew()
ClassList = All.ClassListMaker(DATA)
GradeList = All.GradeListMaker(DATA)
for i in GradeList:
  Path("CollectedData/"+i).mkdir(parents=True, exist_ok=True)
for i in ClassList:
  MainList = i.split("-")
  Path("CollectedData/"+MainList[0]+"/"+MainList[0]+MainList[1]).mkdir(parents=True, exist_ok=True)
  Path("CollectedData/"+MainList[0]+"/"+MainList[0]+MainList[1]+"/"+MainList[0]+MainList[1]+"Student").mkdir(parents=True, exist_ok=True)
All.main(DATA)
NewData = All.DataFunction(DATA)
ClassList = All.ClassListMaker(NewData)
GradeList = All.GradeListMaker(NewData)
for i in GradeList:
  Path("CollectedData/"+i).mkdir(parents=True, exist_ok=True)
for i in ClassList:
  MainList = i.split("-")
  Path("CollectedData/"+MainList[0]+"/"+MainList[0]+MainList[1]).mkdir(parents=True, exist_ok=True)
  Path("CollectedData/"+MainList[0]+"/"+MainList[0]+MainList[1]+"/"+MainList[0]+MainList[1]+"Student").mkdir(parents=True, exist_ok=True)
All.main(NewData)
Z=All.SectionFileInput(NewData)
All.SectionFileMaker(Z)
Z3=All.SectionAggregateSorter(NewData) 
All.SectionAggregateMaker(Z3)
if NewData not in [None,{}]:
  f = open("DATA.txt", "w")
  f.write(str(NewData))
  f.close()
else:
  f = open("DATA.txt", "w")
  f.write("None")
  f.close()


