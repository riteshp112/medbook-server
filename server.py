from crypt import methods
from urllib import response
from flask import Flask, jsonify, request ,redirect,Response
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
@app.route("/post",methods=['POST'])
def post():
  a=dict(request.json)
  a=dict(a)
  client = pymongo.MongoClient("mongodb+srv://riteshp112:6O8yYtaH1KvOaeyz@ritesh.l5gt1.mongodb.net/testdb?retryWrites=true&w=majority&authSource=admin")
  db = client[ "testdb" ]
  col = db[ "post" ]
  x=col.insert_one(a)
  return ""
@app.route("/check",methods=['GET','POST'])
def show():
  return "Sever is running OK"
@app.route("/login",methods=["GET","POST"])
def login():
  a=dict(request.json)
  client = pymongo.MongoClient("mongodb+srv://riteshp112:6O8yYtaH1KvOaeyz@ritesh.l5gt1.mongodb.net/testdb?retryWrites=true&w=majority&authSource=admin",connect=False)
  db = client[ "testdb" ]
  col = db[ "testcol" ]
  res=col.find(a)
  res=list(res)
  if len(res)==0:
    return Response(headers={'hua':'nahi'})
  else:
    return Response(headers={'hua':'ha'})
  return ""
@app.route("/home",methods=["GET","POST"])
def home():
  a=dict(request.json)
  client = pymongo.MongoClient("mongodb+srv://riteshp112:6O8yYtaH1KvOaeyz@ritesh.l5gt1.mongodb.net/testdb?retryWrites=true&w=majority&authSource=admin",connect=False)
  db = client[ "testdb" ]
  col = db[ "post" ]
  res=col.find()
  posts={}
  i=0
  a=int(a["plen"])
  resf=res[:a+5]
  for item in resf:
    posts[str(i)]={"use":item["use"],"post":item["post"]}
    i+=1
  return Response(headers={"content":posts})
  return ""