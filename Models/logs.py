# import libraries
from pymongo import MongoClient

#class 
class operations:
    #constructor 
    def __init__(self):
        self.client = MongoClient('localhost',27017)

    #get DB name
    def get_db(self, dbname):
        return self.client[dbname]

    def insert_logs(self, dbname, collection_name, insertion_data):
        db = self.get_db(dbname)
        return db[collection_name].insert(insertion_data)