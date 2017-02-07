from pymongo import MongoClient
from collections import defaultdict
from pprint import pprint
import urllib2
import csv

def getTeachersDicts():
    teachersFile = open("data/teachers.csv")
    teachersReader = csv.DictReader(teachersFile)
    teachers = []
    for teacher in teacherReader:
        pInfo = defaultdict(list)
        pInfo["code"] = teacher["code"]
        pInfo["teacher"] = teacher["teacher"]
        pInfo["period"] = teacher["period"]
        teachers.append(pInfo)
    teachersFile.close()
    return teachers



def isLocalConnection():
    try:
        urllib2.urlopen('http://lisa.stuy.edu', timeout=1)
        return True
    except urllib2.URLError as err: 
        return False


if __name__ == "__main__":
    allTeachersInfo = getTeachersDicts()
    pprint(allTeachersInfo)

    if isLocalConnection():
        c = MongoClient('lisa.stuy.edu', 27017)
        db = c['pokeMONGO_champions']
        db.teachers.drop()
        for teacher in allTeachersInfo:
            studentsInCourse = db.students.find( {"courses.code" : teacher.code} )
            ids = []
            for student in studentsInCourse:
                ids.append(student["id"])
            teacher["sIds"] = ids
        pass #UNTESTED  
    else:
        print "Not in Lisa :( ssh there first!"
    print "Done."
