
from pymongo import MongoClient
from collections import defaultdict
from pprint import pprint
import urllib2
import csv



def getPeepsDicts():
    peepsFile = open("data/peeps.csv")
    peepReader = csv.DictReader(peepsFile)
    peeps = []
    for peep in peepReader:
        pInfo = defaultdict(list)
        pInfo["name"] = peep["name"]
        pInfo["age"] = peep["age"]
        pInfo["id"] = peep["id"]
        peeps.append(pInfo)
    peepsFile.close()
    return peeps



def getCoursesDicts():
    coursesFile = open("data/courses.csv")
    courseReader = csv.DictReader(coursesFile)
    courses = []
    for course in courseReader:
        pInfo = {}
        pInfo["code"] = course["code"]
        pInfo["mark"] = course["mark"]
        pInfo["id"] = course["id"]
        courses.append(pInfo)
    coursesFile.close()
    return courses



# pair peeps info with courses info
def getAllStudentInfo():
    peepsList = getPeepsDicts()
    coursesList = getCoursesDicts()

    d = defaultdict(dict)
    for peep in peepsList:
        d[ peep["id"] ] = peep

    for course in coursesList:
        id_from_course = course["id"]
        course.pop("id") # not needed!
        # courses goes into "courses" list in student dict
        d[id_from_course]["courses"].append( course )

    return d.values()
    


def isLocalConnection():
    try:
        urllib2.urlopen('http://lisa.stuy.edu', timeout=1)
        return True
    except urllib2.URLError as err: 
        return False


    
if __name__ == "__main__":
    allStudentInfo = getAllStudentInfo()
    pprint(allStudentInfo)
    
    if isLocalConnection():
        c = MongoClient('lisa.stuy.edu', 27017)
        db = c['pokeMONGO_champions']
        db.students.drop()
        db.students.insert_many( getAllStudentInfo() )
    else:
        print "Not in Lisa :( ssh there first!"
        
    print "Done."
