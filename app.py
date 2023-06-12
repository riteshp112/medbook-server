import json
from flask import Flask, request
from flask_cors import CORS
from myMailer import MailSender
from index import OPERATIONS
from utils import parseRequest
from connections import db

app = Flask(__name__)
CORS(app)


@app.route("/invoke", methods=["GET", "POST"])
def invoke():
    invokeRequest = {}
    try:
        if request and request.json:
            invokeRequest = dict(request.json)
            invokeRequest = json.dumps(invokeRequest)
            invokeRequest = json.loads(invokeRequest, object_hook=parseRequest)
            return OPERATIONS[invokeRequest["type"]](invokeRequest)
        else:
            return "Server is running ok"
    except Exception as e:
        return {"response": {"error": str(e) + ": body " + str(invokeRequest)}}


@app.route("/sendMail", methods=["GET", "POST"])
def sendMail():
    invokeRequest = dict(request.json)
    invokeRequest = json.dumps(invokeRequest)
    invokeRequest = json.loads(invokeRequest, object_hook=parseRequest)
    res = MailSender(invokeRequest)
    return {"response": {"result": str(res)}}


@app.route("/goodMorning", methods=["GET", "POST"])
def sendGoodMorning():
    users = db["testcol"].find()
    users = list(users)
    userEmails = [
        {"name": user.get("name"), "email": user.get("email","")} for user in users
    ]
    print(users)
    invokeRequest = dict(
        {
            "subject": "Good Morning",
            "sender": {"name": "Ritesh Patel", "email": "riteshp112@gmail.com"},
            "reply_to": {"name": "Ritesh Patel", "email": "riteshp112@gmail.com"},
            "to": userEmails,
            "html_content": "<text>Dear User , </b> Good Morning</text>",
        }
    )
    res = MailSender(invokeRequest)
    return {"response": {"result": str(res)}}


if __name__ == "__main__":
    app.run(debug=True)
