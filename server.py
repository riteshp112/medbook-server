from crypt import methods
from urllib import response
from flask import Flask, jsonify, request ,redirect
import pymongo
app=Flask(__name__)
@app.route("/users",methods=['POST'])
def users():
  a=dict(request.json)
  a=dict(a)
  client = pymongo.MongoClient("mongodb+srv://riteshp112:6O8yYtaH1KvOaeyz@ritesh.l5gt1.mongodb.net/testdb?retryWrites=true&w=majority&authSource=admin")
  db = client[ "testdb" ]
  col = db[ "testcol" ]
  x=col.insert_one(a)
  return ""
@app.route("/show",methods=['GET','POST'])
def show():
  print("show")
  return ""
@app.route("/login",methods=["GET","POST"])
def login():
  a=dict(request.json)
  client = pymongo.MongoClient("mongodb+srv://riteshp112:6O8yYtaH1KvOaeyz@ritesh.l5gt1.mongodb.net/testdb?retryWrites=true&w=majority&authSource=admin",connect=False)
  db = client[ "testdb" ]
  col = db[ "testcol" ]
  res=col.find(a)
  res=list(res)
  if len(res)==0:
    response.update({"status:500"})
  else:
    response.update({"status:200"})
  return ""