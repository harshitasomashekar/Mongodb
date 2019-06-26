from pymongo import MongoClient
import pandas as pd
# to check the connection
try:
    client = MongoClient()
    print("Connected successfully!!!")

    db=client.stocks
    collection = db.day7
    cf = pd.read_csv("day7.csv")  # csv file which you want to import
    records_ = cf.to_dict(orient = 'records')
    result = collection.insert_many(records_ )
except:
    print("Could not connect to MongoDB")

