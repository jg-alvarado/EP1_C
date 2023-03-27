import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["inventario"]
collection = db["productos"]

