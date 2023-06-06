import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["employee_asset_management"]