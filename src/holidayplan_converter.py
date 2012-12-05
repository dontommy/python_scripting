'''
Created on Nov 27, 2012

@author: dontommy
'''
myFile = open("ferie5.txt")

wdays = ["mandag","tirsdag","onsdag","torsdag","fredag","lørdag","søndag"]

def GetMonth(dateline):
    dateline = dateline.strip(" ")
    el = dateline.split(" ")
    if el[2] == "januar":
        month = 1
    elif el[2] == "februar":
        month = 2
    elif el[2] == "marts":
        month = 3
    elif el[2] == "april":
        month = 4
    elif el[2] == "maj":
        month = 5
    elif el[2] == "juni":
        month = 6
    elif el[2] == "juli":
        month = 7
    elif el[2] == "august":
        month = 8
    elif el[2] == "september":
        month = 9
    elif el[2] == "oktober":
        month = 10
    elif el[2] == "november":
        month = 11
    else:
        month = 12
    month = str(month)
    dagen = str(el[1])
    dagen = dagen.strip(".,()")
    thedate = dagen+"/"+month+"/"+el[3]
    thedate = thedate.strip(".,()")
    thedate = thedate.strip("\n")
    return thedate
    
theDirs = []
count = 0
while True:
    thesplit = 0
    meltjek = 0
    Desc = myFile.readline()
    Desc = str(Desc.replace("(", ""))
    Desc = Desc.replace(")","")
    Desc = Desc.replace("\n","")
    Desc = Desc.replace("/","")
    Desc = Desc.replace("\\","")
    if Desc == "":
        break
    if "Ferieplan" in Desc:
        continue
    Desc1 = str(Desc)
    TestDesc = Desc1.split(" ")
    for test2 in TestDesc:
        if test2 in wdays:
            if meltjek == 0:
                DagTjek = " ".join(TestDesc)
                DagTjek = DagTjek.split(test2)
                Desc = DagTjek[0]
                Desc = Desc.strip(" ")
                Daton = "dagen"+DagTjek[1]         
                meltjek = 1
                thesplit = 1
    Desc = Desc.strip('\n')
    if thesplit == 1:
        pass
    else:
        Daton = myFile.readline()
    if not "-" in Daton:
        StartDate = Daton
        EndDate = Daton
    else:
        Dato = Daton.split("-")
        StartDate = Dato[0]
        EndDate = Dato[1]
    if not len(EndDate) <= 30:
        break
    StartDate = GetMonth(StartDate)
    EndDate = GetMonth(EndDate)
    count = count+1
    theDirs.append({"Desc" : Desc,"StartDate" : StartDate,"EndDate" : EndDate})

print("Number of holiday(s): ",count)
for shit in theDirs:
    print(shit)