import ast
import json
from flask import Flask, request
import pymongo
from flask_cors import CORS
from bson.objectid import ObjectId
from config import MONGO_URI
from myMailer import MailSender

app = Flask(__name__)
CORS(app)


@app.route("/invoke", methods=["GET", "POST"])
def invoke():

    invokeRequest = dict(request.json)
    client = pymongo.MongoClient(
        MONGO_URI,
        connect=False,
    )
    invokeRequest = ast.literal_eval(json.dumps(invokeRequest))
    print(invokeRequest)
    invokeType = invokeRequest["type"]
    if invokeType == "insert":
        table = invokeRequest["table"]
        data = invokeRequest["data"]
        res = client["testdb"][table].insert_one(data)
        return {"response": {"iserted_id": str(res.inserted_id)}}
    elif invokeType == "update":
        table = invokeRequest["table"]
        id = invokeRequest["id"]
        changes = invokeRequest["changes"]
        myquery = {"_id": ObjectId(id)}
        res = client["testdb"][table].update_one(myquery, changes)
        return {
            "response": {
                "raw_result": str(res.raw_result),
                "upserted_id": res.upserted_id,
                "modified_count": res.modified_count,
                "matched_count": res.matched_count,
                "acknowledged": res.acknowledged,
            }
        }
    elif invokeType == "select":
        print(str(request))
        table = invokeRequest["table"]
        condition = invokeRequest["condition"]
        limit = int(invokeRequest["limit"])
        data = client["testdb"][table].find(condition)
        data = list(data)[::-1]
        data = data[:limit]
        for item in data:
            item["_id"] = str(item["_id"])
        return {"response": data}
    return {"response": "Server Running OK"}


@app.route("/sendMail", methods=["GET", "POST"])
def sendMail():
    invokeRequest = dict(request.json)
    res = MailSender(invokeRequest)
    return {"response": str(res)}


if __name__ == "__main__":
    app.run(debug=True)
