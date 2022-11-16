import json
from connections import db
from bson.objectid import ObjectId
from collections import defaultdict
from operator import itemgetter
from utils import parse_json


def select(params):
    table, condition, limit = itemgetter("table", "condition", "limit")(params)
    data = db[table].find(condition).sort([("_id", -1)]).limit(limit)
    data = list(data)
    return {"response": parse_json(data)}


def update(params):
    id, table, changes = itemgetter("id", "table", "changes")(params)
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
    table, data = itemgetter("table", "data")(params)
    res = db[table].insert_one(data)
    return {"response": {"iserted_id": str(res.inserted_id)}}


def invalidOperation(params):
    return {"response": "Invalid Operation with parameters " + str(params)}


OPERATIONS = defaultdict(
    lambda: invalidOperation, {"update": update, "select": select, "insert": insert}
)
