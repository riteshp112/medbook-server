import ast
import json
from flask import Flask, request
from flask_cors import CORS
from myMailer import MailSender
from operations import OPERATIONS

app = Flask(__name__)
CORS(app)


@app.route("/invoke", methods=["GET", "POST"])
def invoke():
    invokeRequest = dict(request.json)
    return OPERATIONS[invokeRequest['type']](invokeRequest)


@app.route("/sendMail", methods=["GET", "POST"])
def sendMail():
    invokeRequest = dict(request.json)
    res = MailSender(invokeRequest)
    return {"response": str(res)}


if __name__ == "__main__":
    app.run(debug=True)
