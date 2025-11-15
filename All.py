import os
import csv
import All
from pathlib import Path
import shutil

def PersonalDetailsNew():
  Name = input("Enter Full Name: ")
  AdmissionNo = int(input("Enter Admission Number: "))
  DOB = input("Enter Date of Birth (DD/MM/YYYY): ")
  AttendencePercent = int(input("Enter Attendance in %: "))
  BoardRollNo = int(input("Enter Board Roll Number (0 for students not currently in X/XII): "))
  Grade = input("Enter Grade: ")
  Section = input("Enter Section: ")
  ClassRollNo = int(input("Enter Class Roll Number: "))
  MothersName = input("Enter Mother's Name: ")
  FathersName = input("Enter Father's Name: ")
  Details ={"Name":Name.upper(),"AdmissionNo":AdmissionNo,"DOB":DOB,"Attendance":AttendencePercent,"Boardrollno":BoardRollNo,"Grade":Grade.upper(),"Classrollno":ClassRollNo,"Section":Section.upper(),"MothersName":MothersName.upper(),"FathersName":FathersName.upper()}
  return Details
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
def SubjectInputNew():

    Subjects = []

    while True:
        LanguageSubject = input("Enter Language Subject: ")
        if LanguageSubject not in ["English", "Hindi"]:
            print("That is not a language subject offered by the school!")
            print("Please enter English or Hindi")
            pass
        else:
            break
    Subjects.append(LanguageSubject)

    CoreSubjects = []
    while True:
        print("\nList of Core Subjects (XI/XII): ")
        print(
            "\n Non Medical = Physics, Chemistry, Maths\n Medical = Physics, Chemistry, Biology\n Commerce = Accountancy, Economics, Business Studies, Maths\n Arts = History, Political Science, Economics\n Other = Other/Not in XI or XII"
        )
        Stream = input("\nEnter Core Stream: ")
        if Stream == "Non Medical":
            CoreSubjects = ['Physics', 'Chemistry', 'Maths']
        elif Stream == "Medical":
            CoreSubjects = ['Physics', 'Chemistry', 'Biology']
        elif Stream == "Commerce":
            CoreSubjects = [
                'Accounts', 'Economics', 'Business Studies', 'Maths'
            ]
        elif Stream == "Arts":
            CoreSubjects = ['History', 'Political Science', 'Economics']
        elif Stream == "Other":
            n = int(input("\nEnter the number of subjects in Core Stream: "))
            for i in range(n):
                sub = input("Enter Subject Name: ")
                CoreSubjects.append(sub)
        else:
            print("\nPlease enter a valid choice!")
            continue
        for j in CoreSubjects:
            Subjects.append(j)
        break

    while True:
        print(
            "\nList of Optional Subjects:\n Computer Science\n Artificial Intelligence\n Information Technology\n Informatics Practices\n Economics\n Biology\n Maths\n Painting\n Physical Education\n Psychology\n "
        )
        OptionalSubject = input("\nEnter Optional Subject: ")
        if OptionalSubject in Subjects:
            print("\nPlease do not repeat any subject!")
        else:
            Subjects.append(OptionalSubject)
            break

    SixthPlus = int(input("\nEnter number of additional subjects: "))
    if SixthPlus != 0:
        for i in range(SixthPlus):
            while True:
                sub = input("Enter Subject Name: ")
                if sub in Subjects:
                    print("\nPlease do not repeat any subject!")
                else:
                    Subjects.append(sub)
                    break
    return Subjects
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
def SubjectMarksNew(SubjectsList):
  Marks = {}
  NumSubjects = len(SubjectsList)

  EightyTwenty = [
    'English', 'Hindi', 'Maths', 'Accountancy', 'Economics',
    'Business Studies', 'History', 'Political Science', 'Science', 'Social Science'
  ]
  SeventyThirty = [
    'Physics', 'Chemistry', 'Biology', 'Computer Science',
    'Informatics Practices', 'Physical Education', 'Psychology'
  ]
  FiftyFifty = ['Artificial Intelligence', 'Information Technology']
  ThirtySeventy = ['Painting']

  for i in range(NumSubjects):
    p = 0
    if SubjectsList[i] in EightyTwenty:
        while p == 0:
            TheoryMarks = int(input(f"Enter Theory Marks (Max 80) for {SubjectsList[i]}: "))
            PracticalMarks = int(input(f"Enter Practical Marks (Max 20) for {SubjectsList[i]}: "))
            if TheoryMarks > 80 or PracticalMarks > 20:
                p = 0
                print("Invalid marks, Please enter marks again.")
            else:
                p = 1
    elif SubjectsList[i] in SeventyThirty:
        while p == 0:
            TheoryMarks = int(input(f"Enter Theory Marks (Max 70) for {SubjectsList[i]}: "))
            PracticalMarks = int(input(f"Enter Practical Marks (Max 30) for {SubjectsList[i]}: "))
            if TheoryMarks > 70 or PracticalMarks > 30:
                p = 0
                print("Invalid marks, Please enter marks again.")
            else:
                p = 1
    elif SubjectsList[i] in FiftyFifty:
        while p == 0:
            TheoryMarks = int(input(f"Enter Theory Marks (Max 50) for {SubjectsList[i]}: "))
            PracticalMarks = int(input(f"Enter Practical Marks (Max 20) for {SubjectsList[i]}: "))
            if TheoryMarks > 50 or PracticalMarks > 50:
                p = 0
                print("Invalid marks, Please enter marks again.")
            else:
                p = 1    
    elif SubjectsList[i] in ThirtySeventy:
        while p == 0:
            TheoryMarks = int(input(f"Enter Theory Marks (Max 30) for {SubjectsList[i]}: "))
            PracticalMarks = int(input(f"Enter Practical Marks (Max 70) for {SubjectsList[i]}: "))
            if TheoryMarks > 30 or PracticalMarks > 70:
                p = 0
                print("Invalid marks, Please enter marks again.")
            else:
                p = 1
    TotalMarks = TheoryMarks + PracticalMarks
    SubjectMarks = (TheoryMarks, PracticalMarks, TotalMarks)
    Marks[SubjectsList[i]] = SubjectMarks
  return Marks
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
import All
def MainInputNew():
  N = int(input("Enter number of records to be inputted: "))
  DataDict = {}
  for i in range(N):
    PersonalDetails = All.PersonalDetailsNew()
    SubjectsList = All.SubjectInputNew()
    SubjectMarks = All.SubjectMarksNew(SubjectsList)
    Awn = [PersonalDetails,SubjectsList,SubjectMarks]
    DataDict[PersonalDetails["AdmissionNo"]] = Awn
  return DataDict
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
import csv
def PersonalFileNew(AdmissionNo,Data):
  StudentData = Data[AdmissionNo]
  StudentPersonalDataDict = StudentData[0]
  StudentSubjects = StudentData[1]
  StudentMarksDict = StudentData[2]
  Class = StudentPersonalDataDict["Grade"]
  Section = StudentPersonalDataDict["Section"]
  RollNo = StudentPersonalDataDict["Classrollno"]
  Name = StudentPersonalDataDict["Name"]
  FileName = "CollectedData/"+Class +"/"+Class+Section+"/"+Class+Section+"Student/" + "0" + str(RollNo) + "_" + Name + ".csv"
  f = open(FileName, 'w')
  csv_writer = csv.writer(f, delimiter=",")
  feilds =["SNo","Subject","TheoryMarks","PracticalMarks","TotalMarks","Aggregate"]
  rows = []
  TotalMarks = 0
  for i in range(len(StudentSubjects)):
    Subject = StudentSubjects[i]
    Knas = [i+1,Subject,StudentMarksDict[Subject][0],StudentMarksDict[Subject][1],StudentMarksDict[Subject][2],""]
    rows.append(Knas)
    TotalMarks += StudentMarksDict[Subject][2]
  AggreatedMarks = TotalMarks/len(StudentSubjects)
  rows.append(["","","","","",AggreatedMarks])
  csv_writer.writerow(feilds)  
  for i in range(len(rows)):
    csv_writer.writerow(rows[i])
  f.close()
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
import numpy
import matplotlib.pyplot as plt 

def SubjectsGraphNew(Name,csvfile):

 SMInfo=[]
 Subjects=[]
 TheoryMarks=[]
 PracticalMarks=[]
 za = csvfile
 za = za[:-4]

 with open(csvfile, "r") as f:
     y=f.readlines()
     del(y[0])
     del(y[-1])
     for i in y:
         z=i.split(",")
         Sub=z[1]
         Mar=(int(z[2]),int(z[3]))
         SMInfo.append([Sub,Mar])

 for i in SMInfo:
    Subjects.append(i[0])
    TheoryMarks.append(i[1][0])
    PracticalMarks.append(i[1][1])

 plt.xlabel("Subject")
 plt.ylabel("Marks")
 plt.title(f"Marks Subject Distribution for {Name}")

 x = Subjects
 y1 = TheoryMarks
 y2 = PracticalMarks

 plt.bar(x, y1, color='r', width=0.5)
 plt.bar(x, y2, bottom=y1, color='b', width=0.5)
 plt.ylim(0,100)
 plt.legend(["Theory Marks", "Practical Marks"])
 plt.savefig(za)
 plt.clf()
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
import csv

def BarGraphImplimenterNew(Data):
  KeyList = Data.keys()
  for i in KeyList:  
    StudentData = Data[i]
    StudentPersonalDataDict = StudentData[0]
    Class = StudentPersonalDataDict["Grade"]
    Section = StudentPersonalDataDict["Section"]
    RollNo = StudentPersonalDataDict["Classrollno"]
    Name = StudentPersonalDataDict["Name"]
    FileName = "CollectedData/"+Class +"/"+Class+Section+"/"+Class+Section+"Student/" + "0" + str(RollNo) + "_" + Name + ".csv"
    SubjectsGraphNew(Name,FileName)
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy
import csv

def PieChartMakerNew(Name,csvfile):

 SMInfo=[]
 Subjects=[]
 TotalMarks=[]
 Z = csvfile[:-4]+"Pi"

 with open(csvfile, "r") as f:
     y=f.readlines()
     del(y[0])
     del(y[-1])
     for i in y:
         z=i.split(",")
         Sub=z[1]
         Mar=int(z[4])
         SMInfo.append((Sub,Mar))
     SMInfo=sorted(SMInfo,reverse=True,key=lambda x:x[1])

 for i in SMInfo:
    Subjects.append(i[0])
    TotalMarks.append(i[1])

 explode = [0.1]+[x*0 for x in range(len(Subjects)-1)]

 plt.pie(TotalMarks, labels=Subjects, explode=explode, 
 autopct='%0.1f%%', shadow=True, startangle=10)
 plt.title(f"Aggregate Distribution for {Name}")
 plt.savefig(Z)
 plt.clf()
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
import csv

def PieChartImplimenterNew(Data):
  KeyList = Data.keys()
  for i in KeyList:  
    StudentData = Data[i]
    StudentPersonalDataDict = StudentData[0]
    Class = StudentPersonalDataDict["Grade"]
    Section = StudentPersonalDataDict["Section"]
    RollNo = StudentPersonalDataDict["Classrollno"]
    Name = StudentPersonalDataDict["Name"]
    FileName = "CollectedData/"+Class +"/"+Class+Section+"/"+Class+Section+"Student/" + "0" + str(RollNo) + "_" + Name + ".csv"
    PieChartMakerNew(Name,FileName)
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
def AggregateCalculator(SubjectMarks):
    NoOfSubjects=len(SubjectMarks)
    SubSum=0

    for Subject in SubjectMarks:
        SubSum+=SubjectMarks[Subject][2]

    Agg=SubSum/NoOfSubjects

    return Agg
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
def SectionFileInput(Data):
    ClassList = All.ClassListMaker(Data)
    AllClassData={}
    SingleClassData=[]

    for Class in ClassList: 
        SingleClassData=[]
        for UniqueKey in Data: 
            StudentData=[]
            if str(Data[UniqueKey][0]['Grade']+"-"+Data[UniqueKey][0]['Section']) == Class:  
                ClassRN=Data[UniqueKey][0]['Classrollno']
                Name=Data[UniqueKey][0]['Name']
                Atten=Data[UniqueKey][0]['Attendance']  
                BoardRN=Data[UniqueKey][0]['Boardrollno']
                SubjectsList=Data[UniqueKey][1]
                Subjects=""
                for i in SubjectsList:
                    if i!=SubjectsList[0]:
                        Subjects=Subjects+", "+i
                    else:
                        Subjects=Subjects+i
                SubjectMarks=Data[UniqueKey][2]
                Aggregate=AggregateCalculator(SubjectMarks)
                StudentData=[ClassRN,Name,Atten,BoardRN,Subjects,Aggregate]
                SingleClassData.append(StudentData)
        SingleClassData.sort(key=lambda x: x[0])
        AllClassData[Class]=SingleClassData

    return AllClassData
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
def SectionFileMaker(Data):
    CSVFields=["Roll Number", "Name", "Attendance", "Board Roll Number", "Subjects","Aggregate"]

    for Class in Data:
        ClassName=Class.partition("-")
        filename="CollectedData/"+ClassName[0]+"/"+ClassName[0]+ClassName[2]+"/"+ClassName[0]+ClassName[2]+".csv"
        file=open(file=filename,mode='w',newline="")
        writer=csv.writer(file)
        writer.writerow(CSVFields)
        for Student in Data[Class]:  
            ClassRN=Student[0]
            Name=Student[1]
            Attendance=Student[2]
            BoardRN=Student[3]
            Subjects=Student[4]
            Aggregate=Student[5]
            AppendData=[str(ClassRN),Name,str(Attendance),str(BoardRN),Subjects,str(Aggregate)]
            writer.writerow(AppendData)
        file.close()


#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------


def SectionAggregateSorter(Data):   
    ClassList = All.ClassListMaker(Data)
    AllClassData={}
    SingleClassData=[]

    for Class in ClassList: 
        SingleClassData=[]
        for UniqueKey in Data: 
            StudentData=[]
            if str(Data[UniqueKey][0]['Grade']+"-"+Data[UniqueKey][0]['Section']) == Class:  
                Name=Data[UniqueKey][0]['Name']
                SubjectsList=Data[UniqueKey][1]
                Subjects=""
                for i in SubjectsList:
                    if i!=SubjectsList[0]:
                        Subjects=Subjects+", "+i
                    else:
                        Subjects=Subjects+i
                SubjectMarks=Data[UniqueKey][2]
                Aggregate=AggregateCalculator(SubjectMarks)
                StudentData=[Name,Aggregate]
                SingleClassData.append(StudentData)
        SingleClassData.sort(key=lambda x: x[1], reverse=True)
        AllClassData[Class]=SingleClassData
    return AllClassData


#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------


def SectionAggregateMaker(Data):
    CSVFields=["S. No.", "Name","Aggregate"]

    for Class in Data:
        ClassName=Class.partition("-")
        filename="CollectedData/"+ClassName[0]+"/"+ClassName[0]+ClassName[2]+"/"+ClassName[0]+ClassName[2]+"Top5.csv"
        file=open(file=filename,mode='w',newline="")
        writer=csv.writer(file)
        writer.writerow(CSVFields)
        for i in range(len(Data[Class])):  
            if i<=4:
                Student=Data[Class][i] 
                Name=Student[0]
                Aggregate=Student[1]
                SNo=i+1
                AppendData=[str(SNo),Name,str(Aggregate)]
                writer.writerow(AppendData)
            else:
                break
        file.close()


#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------


def main(DATA):
  AdmisList = DATA.keys()
  for i in AdmisList:
    PersonalFileNew(i,DATA)
  BarGraphImplimenterNew(DATA)
  PieChartImplimenterNew(DATA)
  Z=SectionFileInput(DATA)
  SectionFileMaker(Z)
  Z3=SectionAggregateSorter(DATA) 
  SectionAggregateMaker(Z3)


#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------


def search(AdmissionNo,DATA):
    Datakeys = DATA.keys()
    k = 0
    if AdmissionNo not in Datakeys:
        print("Admission Number specified is not present.")
        k = 1
        return None
    if k == 0:
        PersonsData = DATA[AdmissionNo]
        return PersonsData

        
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

def delete(AdmissionNo,DATA):
    personal_unrefined_data = search(AdmissionNo,DATA)
    if personal_unrefined_data == None:
        PersonalData = None
    else:
        PersonalData =  personal_unrefined_data[0]
        Class = PersonalData["Grade"]
        Section = PersonalData["Section"]
        RollNo = PersonalData["Classrollno"]
        Name = PersonalData["Name"]
        FileName1 = "CollectedData/"+Class +"/"+Class+Section+"/"+Class+Section+"Student/" + "0" + str(RollNo) + "_" + Name + ".csv"
        FileName2 = "CollectedData/"+Class +"/"+Class+Section+"/"+Class+Section+"Student/" + "0" + str(RollNo) + "_" + Name + ".png"
        FileName3 = "CollectedData/"+Class +"/"+Class+Section+"/"+Class+Section+"Student/" + "0" + str(RollNo) + "_" + Name +"Pi"+ ".png"
        os.remove(FileName1)
        os.remove(FileName2)
        os.remove(FileName3)
        del DATA[AdmissionNo]
    return DATA


#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

def personal_data_modify(AdmissionNo,DATA):
    Personal_Unrefined_Data = search(AdmissionNo,DATA)
    if Personal_Unrefined_Data == None:
        PersonalData = None
        print("DATA NOT PRESENT")
        return None
    else:
        print("You can Modify the following data: Name, AdmissionNo, DOB, Attendance, Boardrollno, Grade, Classrollno, Section, MothersName, FathersName")
        print('Eg: \nType "Section" If you want to change the section.\nType "Name,DOB,Attendance" if you want to change the Name, Date of Birth, and Attendance respectively.')
        CriteriaChange = input("Enter what to change: ")
        AllCriterias = CriteriaChange.split(",")
        if "AdmissionNo" in AllCriterias:
            AdmissionNewNo = int(input("Enter new Admission No:"))
            DATA[AdmissionNewNo] =Personal_Unrefined_Data
            DATA[AdmissionNewNo][0]["AdmissionNo"] = AdmissionNewNo
            del DATA[AdmissionNo]
            AdmissionNo = AdmissionNewNo
            for i in range(len(AllCriterias)):
                if AllCriterias[i] == "AdmissionNo":
                    AllCriterias.pop(i)
                    break
        else:
            AdmissionNewNo = 0
        for i in AllCriterias:
            datainput = input("Enter new "+i+":")
            if i not in [ "Name","DOB","Grade","Section","MothersName","FathersName"]:
                datainput = int(datainput)
            DATA[AdmissionNo][0][i] = datainput
        return [DATA,AdmissionNewNo]
        
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

def subject_list_data_modify(AdmissionNo,DATA):
    Personal_Unrefined_Data = search(AdmissionNo,DATA)
    if Personal_Unrefined_Data == None:
        PersonalData = None
        print("DATA NOT PRESENT.")
        return None
    else:
        DATA[AdmissionNo] = Personal_Unrefined_Data
        SubjectListNew = SubjectInputNew()
        DATA[AdmissionNo][1] = SubjectListNew
        DATA[AdmissionNo][2] = SubjectMarksNew(SubjectListNew)
        return DATA
        
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

def subject_marks_data_modify(AdmissionNo,DATA):
    Personal_Unrefined_Data = search(AdmissionNo,DATA)
    if Personal_Unrefined_Data == None:
        PersonalData = None
        print("DATA NOT PRESENT.")
        return None
    else:
        DATA[AdmissionNo] = Personal_Unrefined_Data
        DATA[AdmissionNo][2] = SubjectMarksNew(DATA[AdmissionNo][1])
        return DATA
        
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

def modify(AdmissionNo,DATA):
    print("Enter 1 to modify Personal Data.")
    print("Enter 2 to modify Subject List.")
    print("Enter 3 to modify Subject Marks.")
    print("Enter 123 to modify all 3.")
    ConstantA = input("Enter your choice: ")
    worklist = list(ConstantA)
    if AdmissionNo in DATA.keys():
        naha = DATA[AdmissionNo][0]
        Class = naha["Grade"]
        Section = naha["Section"]
        RollNo = naha["Classrollno"]
        Name = naha["Name"]
        FileName1 = "CollectedData/"+Class +"/"+Class+Section+"/"+Class+Section+"Student/" + "0" + str(RollNo) + "_" + Name + ".csv"
        FileName2 = "CollectedData/"+Class +"/"+Class+Section+"/"+Class+Section+"Student/" + "0" + str(RollNo) + "_" + Name + ".png"
        FileName3 = "CollectedData/"+Class +"/"+Class+Section+"/"+Class+Section+"Student/" + "0" + str(RollNo) + "_" + Name +"Pi"+ ".png"
        os.remove(FileName1)
        os.remove(FileName2)
        os.remove(FileName3)
    for i in worklist:
        if i == "1":
            DATAnew = personal_data_modify(AdmissionNo,DATA)
            if DATAnew == None:
                "Nothing"
            else:
                DATA = DATAnew[0]
                if DATAnew[1] != 0:
                    AdmissionNo = DATAnew[1]
        elif i == "2":
            DATAnew = subject_list_data_modify(AdmissionNo,DATA)
            DATA = DATAnew
            if DATAnew == None:
                "Nothing"
        elif i == "3":
            DATAnew = subject_marks_data_modify(AdmissionNo,DATA)
            DATA = DATAnew
            if DATAnew == None:
                "Nothing"
        else:
            print("Invalid Input")
            "Nothing"
    try:
        main(DATA)
    except:
        pass
    return DATA
#---------------------------------------------------------------------------------------------------------------------------------------------
#--------------

def Append(DATA):
  AdmissionNo = int(input("Enter Admission No To Append: "))
  AddableDATA = []
  AddableDATA.append(PersonalDetailsNew())
  Subjectlist = SubjectInputNew()
  AddableDATA.append(Subjectlist)
  AddableDATA.append(SubjectMarksNew(Subjectlist))
  DATA[AdmissionNo] = AddableDATA
  Path("CollectedData/"+AddableDATA[0]["Grade"]).mkdir(parents=True, exist_ok=True)
  Path("CollectedData/"+AddableDATA[0]["Grade"]+"/"+AddableDATA[0]["Grade"]+AddableDATA[0]["Section"]).mkdir(parents=True, exist_ok=True)
  Path("CollectedData/"+AddableDATA[0]["Grade"]+"/"+AddableDATA[0]["Grade"]+AddableDATA[0]["Section"]+"/"+AddableDATA[0]["Grade"]+AddableDATA[0]["Section"]+"Student").mkdir(parents=True, exist_ok=True)
  return DATA
    
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

import os
def DataFunction(DATA):
  print("You can do the following actions: Search(1), Append(2), Modify(3), Delete(4), Clear Data(5)")
  print("Type the suffixed Number to perform the action, any other number will exit the program.")
  print('Eg: \nType "1" If you want to Search for Data.\nType "235" If you want to Append Data, Modify Data and Delete All Data respectively.')
  ConstantK = input("Enter your choice: ")
  worklist = list(ConstantK)
  for i in worklist:
    if i == "1":
      t=0
      while t == 0:
        Admisno = int(input("Enter Admission No To Search:"))
        Personal_Unrefined_Data = search(Admisno,DATA)
        if Personal_Unrefined_Data == None:
          print("DATA NOT PRESENT.")
        else:
            StudentPersonalInfo=Personal_Unrefined_Data

            print("Name: ", StudentPersonalInfo[0]['Name'])
            print("Admission No.: ", StudentPersonalInfo[0]['AdmissionNo'])
            print("Date of Birth: ", StudentPersonalInfo[0]['DOB'])
            print("Attendance: ", str(StudentPersonalInfo[0]['Attendance'])+'%')
            print("Board Roll No.: ", StudentPersonalInfo[0]['Boardrollno'])
            print("Grade: ", StudentPersonalInfo[0]['Grade'])
            print("Section: ", StudentPersonalInfo[0]['Section'])
            print("Class Roll Number: ", StudentPersonalInfo[0]['Classrollno'])
            print("Mother's Name: ", StudentPersonalInfo[0]['MothersName'])
            print("Fathers's Name: ", StudentPersonalInfo[0]['FathersName'])

            for subject in StudentPersonalInfo[1]:
                print('\nStudent Theory Marks in ',subject,': ', StudentPersonalInfo[2][subject][0])
                print('Student Practical Marks in ',subject,': ', StudentPersonalInfo[2][subject][1])
                print('Student Total Marks in ',subject,': ', StudentPersonalInfo[2][subject][2])

        t = int(input("Enter 0 to continue, any other number to stop: "))
    elif i == "2":
      t = 0
      while t == 0:  
        DATA = Append(DATA)
        t = int(input("Enter 0 to continue, any other number to stop: "))
      main(DATA)
    elif i == "3":
      t = 0
      while t == 0:
        AdmissionNo = int(input("Enter Admission Number To Modify:"))
        DATA = modify(AdmissionNo,DATA)
        t = int(input("Enter 0 to continue, any other number to stop: "))
      try:
          main(DATA)
      except:
          pass
    elif i == "4":
      t = 0
      while t == 0:
        AdmissionNo = int(input("Enter Admission Number To Delete:"))
        DATA = delete(AdmissionNo,DATA)
        t = int(input("Enter 0 to continue, any other number to stop: "))
      try:
          main(DATA)
      except:
          pass
    elif i == "5":
      KeyList = DATA.keys()
      NonCopyKeyList = []
      for i in KeyList:
        NonCopyKeyList.append(i)
      for i in NonCopyKeyList:
        PersonalData =  DATA[i][0]
        Class = PersonalData["Grade"]
        Section = PersonalData["Section"]
        RollNo = PersonalData["Classrollno"]
        Name = PersonalData["Name"]
        FileName1 = "CollectedData/"+Class +"/"+Class+Section+"/"+Class+Section+"Student/" + "0" + str(RollNo) + "_" + Name + ".csv"
        FileName2 = "CollectedData/"+Class +"/"+Class+Section+"/"+Class+Section+"Student/" + "0" + str(RollNo) + "_" + Name + ".png"
        FileName3 = "CollectedData/"+Class +"/"+Class+Section+"/"+Class+Section+"Student/" + "0" + str(RollNo) + "_" + Name +"Pi"+ ".png"
        os.remove(FileName1)
        os.remove(FileName2)
        os.remove(FileName3)
        del DATA[i]
      shutil.rmtree("CollectedData")
    else:
        exit()
  return DATA

#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

def ClassListMaker(DATA):
    keylist = DATA.keys()
    ClassList = []
    for i in keylist:
        Class = DATA[i][0]["Grade"]
        Section = DATA[i][0]["Section"]
        MainStr = Class+"-"+Section
        if MainStr not in ClassList:
            ClassList.append(MainStr)
    return ClassList

#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

def GradeListMaker(DATA):
    keylist = DATA.keys()
    GradeList = []
    for i in keylist:
        Grade = DATA[i][0]["Grade"]
        if Grade not in GradeList:
            GradeList.append(Grade)
    return GradeList