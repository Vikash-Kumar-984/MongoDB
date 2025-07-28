# !pip install pymongo
from pymongo import MongoClient

# Connect to the local MongoDB server
client = MongoClient("mongodb://localhost:27017")

# Create or access a database
db = client["mydatabase"]

# Create or access a collection
collection = db["users"]

# Insert a sample document
collection.insert_one({"name": "Vikash", "role": "Admin"})

# Read documents
for doc in collection.find():
    print(doc)

# mongodb://localhost:27017/ 