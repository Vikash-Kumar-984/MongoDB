# 📘 MongoDB Queries & Concepts

A reference guide covering essential MongoDB queries, terms, and code examples using Python (PyMongo) and Mongo Shell.

---

## 📁 Contents
- [🔹 Getting Started](#-getting-started)
- [🔹 CRUD Operations](#-crud-operations)
- [🔹 Aggregation Framework](#-aggregation-framework)
- [🔹 Indexes](#-indexes)
- [🔹 Schema Design](#-schema-design)
- [🔹 Important Terms](#-important-terms)
- [🔹 PyMongo Examples](#-pymongo-examples)

---

## 🔹 Getting Started

```bash
# Start MongoDB
mongod

# Connect to shell
mongo

# Show all databases
show dbs

# Create or switch to a DB
use superstore_db

# Show all collections
show collections
```

---

## 🔹 CRUD Operations

### 📌 Insert Documents
```js
db.orders.insertOne({ name: "Wiry", sales: 500 })
db.orders.insertMany([{ name: "Vikash" }, { name: "Kumar" }])
```

### 📌 Read Documents
```js
db.orders.find()
db.orders.find({ Region: "West" })
```

### 📌 Update Documents
```js
db.orders.updateOne({ name: "Alice" }, { $set: { sales: 550 } })
db.orders.updateMany({ "Ship Mode": "First Class" }, { $set: { "Ship Mode": "Premium Class" } })
```

### 📌 Delete Documents
```js
db.orders.deleteOne({ name: "Kumar" })
db.orders.deleteMany({ sales: { $lt: 50 } })
```

---

## 🔹 Aggregation Framework

```js
// Group and sum sales by region
db.orders.aggregate([
  { $group: { _id: "$Region", totalSales: { $sum: "$Sales" } } }
])

// Filter before grouping
db.orders.aggregate([
  { $match: { Region: "West" } },
  { $group: { _id: "$Category", totalProfit: { $sum: "$Profit" } } }
])
```

---

## 🔹 Indexes

```js
// Create index
db.orders.createIndex({ "Customer Name": 1 })

// View all indexes
db.orders.getIndexes()
```

---

## 🔹 Schema Design

- Use **embedded documents** for tightly related data
- Use **references** when data is large or accessed separately
- Use **validation**:
```js
db.createCollection("products", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["name", "price"]
    }
  }
})
```

---

## 🔹 Important MongoDB Terms

| Term | Meaning |
|------|---------|
| **Document** | Basic unit of data (like a row) in BSON format |
| **Collection** | A group of related documents (like a table) |
| **Database** | Container for collections |
| **Replica Set** | Group of servers for redundancy and failover |
| **Sharding** | Splitting data across servers for horizontal scaling |
| **Aggregation** | Framework to process and transform documents |
| **$match, $group, $project** | Stages in aggregation pipeline |
| **Index** | Structure to improve query speed |
| **Schema Validation** | Optional enforcement of document structure |

---

## 🔹 PyMongo Examples

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["superstore_db"]
collection = db["orders"]

# Find orders from East region
results = collection.find({ "Region": "East" })
for order in results:
    print(order)

# Aggregation: Total sales per category
pipeline = [
    { "$group": { "_id": "$Category", "TotalSales": { "$sum": "$Sales" } } }
]
for doc in collection.aggregate(pipeline):
    print(doc)
```



---

## 📌 Author  
**Vikash Kumar | Data Scientist**

**Feel free to clone, fork, or contribute!
