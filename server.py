from crypt import methods
from urllib import response
from flask import Flask, jsonify, request ,redirect,Response
import pymongo
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
@app.route("/invoke",methods=["GET","POST"])
def invoke():
  invokeRequest=dict(request.json)
  client = pymongo.MongoClient("mongodb+srv://riteshp112:6O8yYtaH1KvOaeyz@ritesh.l5gt1.mongodb.net/testdb?retryWrites=true&w=majority&authSource=admin",connect=False)
  print(invokeRequest)
  invokeType=invokeRequest["type"]
  if invokeType=="insert":
    table=invokeRequest["table"]
    data=invokeRequest["data"]
    res=client["testdb"][table].insert_one(data)
    return Response(headers={"output":res,"Access-Control-Allow-Origin": "*","Access-Control-Allow-Headers":"Content-Type,Authorization","Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,OPTIONS","Access-Control-Allow-Credentials" : True })
  elif invokeType=="update":
    table=invokeRequest["table"]
    id=invokeRequest["id"]
    changes=invokeRequest["changes"]
    myquery = { "_id": id }
    newvalues = { "$set": changes }
    res=client["testdb"][table].update_one(myquery, newvalues)    
    return Response(headers={"output":res,"Access-Control-Allow-Origin": "*","Access-Control-Allow-Headers":"Content-Type,Authorization","Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,OPTIONS","Access-Control-Allow-Credentials" : True })
  elif invokeType=="select":
    print(str(request))
    table=invokeRequest["table"]
    condition=invokeRequest["condition"]
    limit=int(invokeRequest["limit"])
    data=client["testdb"][table].find(condition)
    data=list(data)[:limit]
    for item in data:
      item["_id"]=str(item["_id"])
    return Response(headers={"output":data,"Access-Control-Allow-Origin": "*","Access-Control-Allow-Headers":"*","Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,OPTIONS","Access-Control-Allow-Credentials" : True ,"Content-Type" :"application/json","Cache-Control": "no-cache","Access-Control-Expose-Headers":["output"]})
  return Response(headers={"output":"Please Enter Valid Request","Access-Control-Allow-Origin": "*","Access-Control-Allow-Headers":"Content-Type,Authorization","Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,OPTIONS","Access-Control-Allow-Credentials" : True })

if __name__ == "__main__":
  app.run(debug=True)