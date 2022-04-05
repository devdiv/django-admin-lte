import pymongo

MONGOHOST ='127.0.0.1'
MONGOPOST = 27017
DATABASE = 'onetest'
DBCONNECT = pymongo.MongoClient(host=MONGOHOST,port=MONGOPOST).get_database(DATABASE)