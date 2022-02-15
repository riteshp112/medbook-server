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
@app.route("/show",methods=['GET','POST'])
def show():
  print("show")
  return "Site is running OK"
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
  a=a.plen
  resf=res[a:a+5]
  #l=len(list(res))
  for item in resf:
    posts[str(i)]={"use":item["use"],"post":item["post"]}
    i+=1
  '''temp=len(list(res))
  posts={}
  for item in res:
     posts.update(item) 
  #temp=list(temp)
  if temp==0:
    return Response(data={'hua':'nahi'})
  else:'''
  return Response(headers={"content":posts})
  return ""