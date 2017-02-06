from pymongo import MongoClient
from collections import defaultdict
from pprint import pprint
from __future__ import division
import urllib2
import db_builder


c = MongoClient('lisa.stuy.edu', 27017)
db = c['pokeMONGO_champions']

if __name__ == "__main__":
    allStudentInfo = getAllStudentInfo()
    
    if isLocalConnection():
        students = db.students.find()
        for student in students:
            courses = student["courses"]
            totalScore = 0
            totalAmt = 0
            for course in courses:
                totalScore += grade["mark"]
                totalAmt += 1
            print "%s | %s | %d" % (student["name"], student["id"], totalScore / totalAmt)
    else:
        print "Not in Lisa :( ssh there first!"
        
    print "Done."
