from pymongo import MongoClient

client = MongoClient("mongodb+srv://bikramleeemboo_db_user:dS4HP0EviPPb4KmU@cluster0.2jvdqso.mongodb.net/?appName=Cluster0")
db = client["sewa"]
provinces = db["provinces"]
users = db["users"]
