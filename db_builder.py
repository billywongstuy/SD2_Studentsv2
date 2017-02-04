from pymongo import MongoClient

c = MongoClient('lisa.stuy.edu', 27017)
db = c['pokeMONGO_champions']

d = {'test': 1, 'test2': 2}

db.foo.insert_one(d)
