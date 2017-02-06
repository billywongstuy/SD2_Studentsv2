from __future__ import division
from pymongo import MongoClient
from collections import defaultdict
from pprint import pprint
import urllib2
import db_builder


c = MongoClient('lisa.stuy.edu', 27017)
db = c['pokeMONGO_champions']

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
    else:
        print "Not in Lisa :( ssh there first!"
        
    print "Done."
