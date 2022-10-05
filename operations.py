from connections import db
from bson.objectid import ObjectId
from collections import defaultdict


def select(params):
    table, condition, limit = params
    data = db[table].find(condition)
    data = list(data)[::-1]
    data = data[:limit]
    for item in data:
        item["_id"] = str(item["_id"])
    return {"response": data}


def update(params):
    id, table, changes = params
    myquery = {"_id": ObjectId(id)}
    res = db[table].update_one(myquery, changes)
    return {
        "response": {
            "raw_result": str(res.raw_result),
            "upserted_id": res.upserted_id,
            "modified_count": res.modified_count,
            "matched_count": res.matched_count,
            "acknowledged": res.acknowledged,
        }
    }


def insert(params):
    table, data = params
    res = db[table].insert_one(data)
    return {"response": {"iserted_id": str(res.inserted_id)}}


def invalidOperation(params):
    return {"response": "Invalid Operation"}


OPERATIONS = defaultdict(
    lambda: invalidOperation, {"update": update, "select": select, "insert": insert}
)