from pymongo import MongoClient
import csv


def getPeepsDict():
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



def getCoursesDict():
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



if __name__ == "__main__":
    c = MongoClient('lisa.stuy.edu', 27017)
    db = c['pokeMONGO_champions']
    
    d = {'test': 1, 'test2': 2}
    
    db.foo.insert_one(d)
