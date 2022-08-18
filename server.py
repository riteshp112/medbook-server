import ast
from audioop import reverse
from crypt import methods
import json
from urllib import response
from flask import Flask, jsonify, request ,redirect,Response
import pymongo
from flask_cors import CORS
from bson.objectid import ObjectId
app=Flask(__name__)
CORS(app)
@app.route("/invoke",methods=["GET","POST"])
def invoke():
  invokeRequest=dict(request.json)
  client = pymongo.MongoClient("mongodb+srv://riteshp112:6O8yYtaH1KvOaeyz@ritesh.l5gt1.mongodb.net/testdb?retryWrites=true&w=majority&authSource=admin",connect=False)
  invokeRequest= ast.literal_eval(json.dumps(invokeRequest))
  print(invokeRequest)
  invokeType=invokeRequest["type"]
  if invokeType=="insert":
    table=invokeRequest["table"]
    data=invokeRequest["data"]
    res=client["testdb"][table].insert_one(data)
    return({"response":{"iserted_id":str(res.inserted_id)}})
  elif invokeType=="update":
    table=invokeRequest["table"]
    id=invokeRequest["id"]
    changes=invokeRequest["changes"]
    myquery = { "_id": ObjectId(id) }
    newvalues = { "$set": changes }
    res=client["testdb"][table].update_one(myquery, newvalues)    
    return {"response":{"raw_result":str(res.raw_result),"upserted_id":res.upserted_id,"modified_count":res.modified_count,"matched_count":res.matched_count,"acknowledged":res.acknowledged}}
  elif invokeType=="select":
    print(str(request))
    table=invokeRequest["table"]
    condition=invokeRequest["condition"]
    limit=int(invokeRequest["limit"])
    data=client["testdb"][table].find(condition)
    data=list(data)[::-1]
    data=data[:limit]
    for item in data:
      item["_id"]=str(item["_id"])
    return {"response":data}
  return {"response":"Server Running OK"}

if __name__ == "__main__":
  app.run(debug=True)