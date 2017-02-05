from pymongo import MongoClient
from collections import defaultdict
from pprint import pprint
import csv

def getPeepsDicts():
    peepsFile = open("data/peeps.csv")
    peepReader = csv.DictReader(peepsFile)
    peeps = []
    for peep in peepReader:
        pInfo = {}
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
    peepsInfo = getPeepsDicts()
    coursesInfo = getCoursesDicts()

    d = defaultdict(dict) # no more blank declarations :)
    for L in (peepsInfo, coursesInfo):
        for dictItem in L:
            d[ dictItem["id"] ].update( dictItem ) #combine dicts

    for accumStudentInfo in d.values():
        accumStudentInfo.pop("id") #let mongo add its own ObjectId

    return d.values()
    

if __name__ == "__main__":
    c = MongoClient('lisa.stuy.edu', 27017)
    db = c['pokeMONGO_champions']   
    pprint( getAllStudentInfo() )
    db.foo.insert_many( getAllStudentInfo() )
    print "Done."
