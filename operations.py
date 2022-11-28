import json
from connections import db
from operator import itemgetter


def parseObjectId(obj):
    return str(obj)


def select(params):
    table, condition, limit = itemgetter("table", "condition", "limit")(params)
    data = db[table].find(condition).sort([("_id", -1)]).limit(limit)
    data = list(data)
    return {
        "response": {"result": json.loads(json.dumps(data, default=(parseObjectId)))}
    }


def update(params):
    condition, table, changes = itemgetter("condition", "table", "changes")(params)
    res = db[table].update_one(condition, changes)
    return {
        "response": {
            "result": {
                "raw_result": str(res.raw_result),
                "upserted_id": res.upserted_id,
                "modified_count": res.modified_count,
                "matched_count": res.matched_count,
                "acknowledged": res.acknowledged,
            }
        }
    }


def insert(params):
    table, data = itemgetter("table", "data")(params)
    res = db[table].insert_one(data)
    return {"response": {"result": {"iserted_id": str(res.inserted_id)}}}


def invalidOperation(params):
    return {"response": {"error": "Invalid Operation with parameters " + str(params)}}



