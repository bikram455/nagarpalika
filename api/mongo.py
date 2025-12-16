import os
from pymongo import MongoClient

mongo_url = os.getenv("MONGO_URL")
client = MongoClient(mongo_url)
db = client["sewa"]
provinces = db["provinces"]
users = db["users"]
