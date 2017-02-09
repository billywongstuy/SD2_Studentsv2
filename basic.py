from __future__ import division
from pymongo import MongoClient
from collections import defaultdict
from pprint import pprint
import urllib2
import db_builder


c = MongoClient('lisa.stuy.edu', 27017)
db = c['pokeMONGO_champions']


def getTeachersDicts():
    teachersFile = open("data/teachers.csv")
    teacherReader = csv.DictReader(teachersFile)
    teachers = []
    for teacher in teacherReader:
        pInfo = defaultdict(list)
        pInfo["code"] = teacher["code"]
        pInfo["teacher"] = teacher["teacher"]
        pInfo["period"] = teacher["period"]
        teachers.append(pInfo)
    teachersFile.close()
    return teachers

if __name__ == "__main__":

    if db_builder.isLocalConnection():
        print "NAME" + 12*" " +"ID\tAVERAGE"
        print '-' * 35
        students = db.students.find()
        for student in students:
            courses = student["courses"]
            totalScore = 0
            totalAmt = 0
            for course in courses:
                totalScore += int(course["mark"])
                totalAmt += 1
            name = student["name"]
            diff = 15-len(name)
            name += diff*" "
            average = totalScore / totalAmt
            print "%s\t%s\t%d" % (name, student["id"], average)
            
        allTeachersInfo = getTeachersDicts()
        pprint(allTeachersInfo) 
        
        db.teachers.drop()
        for teacher in allTeachersInfo:
            studentsInCourse = db.students.find( {"courses.code" : teacher["code"]} )
            ids = []
            for student in studentsInCourse:
                ids.append(int(student["id"]))
            teacher["sIds"] = ids
        db.teachers.insert_many( allTeachersInfo )
            
    else:
        print "Not in Lisa :( ssh there first!"
        
    print "Done."
