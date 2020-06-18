# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 14:54:20 2020

@author: Anes ABBAD

@website : https://abbadanes.github.io/

"""
import pymongo

class Database():
    def __init__(self, db_name="Jacques_chirac",client="mongodb://localhost:27017/"):
        mangoclient = pymongo.MongoClient(client)
        self.db_name = db_name
        self.client = mangoclient
        try :
            _ = mangoclient[db_name]
            print("Database created !")
        except :
            print("the database could not be created, are you sure that the client address is accessible?")
     
        
    def create_collection(self,name="posts"):
        try:
            db = self.client[self.db_name]
            col = db[name]
            print("The collection : "+name+" is created in the Database : "+self.db_name)
        except:
            print("The collection could not be created")
        return col
    
    def store(self,collection,posts):
        collection.insert_many(posts)
        print(len(posts)," posts had been stored !")
    

        

        

