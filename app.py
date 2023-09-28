import base64
import json
from flask import Flask, Response, jsonify, request, send_file
from flask_cors import CORS
from myMailer import MailSender
from index import OPERATIONS
from utils import parseRequest
from connections import db
from bson.objectid import ObjectId
from flask_socketio import SocketIO

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")
thread_clients = {}

@app.route("/invoke", methods=["GET", "POST"])
def invoke():
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
    users = db["testcol"].find({"email": {"$exists": True}})
    users = list(users)
    userEmails = [
        {"name": user.get("name"), "email": user.get("email")} for user in users
    ]
    invokeRequest = dict(
        {
            "subject": "Good Morning",
            "sender": {"name": "Ritesh Patel", "email": "riteshp112@gmail.com"},
            "reply_to": {"name": "Ritesh Patel", "email": "riteshp112@gmail.com"},
            "to": userEmails,
            "html_content": "<text>Dear Medbook User , </b> Good Morning</text>",
        }
    )
    res = MailSender(invokeRequest)
    return {"response": {"result": str(res)}}


collection = db["images"]


def allowed_file(filename):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/upload", methods=["POST"])
def upload_image():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        # Save the file to the upload folder
        # Insert image metadata into MongoDB
        file_data = base64.b64encode(file.read()).decode("utf-8")
        file_insert = {"filename": file.filename, "data": file_data}
        result = collection.insert_one(file_insert)

        return (
            jsonify(
                {
                    "message": "File uploaded successfully",
                    "file_id": str(result.inserted_id),
                }
            ),
            200,
        )
    else:
        return jsonify({"error": "Invalid file type"}), 400


@app.route("/retrieve/<file_id>", methods=["GET"])
def retrieve_image(file_id):
    file_data = collection.find_one({"_id": ObjectId(file_id)})

    if not file_data:
        return jsonify({"error": "File not found"}), 404
    decoded_data = base64.b64decode(file_data["data"])
    response = Response(decoded_data, content_type="application/octet-stream")
    response.headers[
        "Content-Disposition"
    ] = f'attachment; filename={file_data["filename"]}'
    return response


@socketio.on("connect")
def handle_connect():
    print("Client connected")


@socketio.on("join_thread")
def join_thread(data):
    thread_id = data["threadId"]
    print(f"Client is joining thread {thread_id}")

    if thread_id not in thread_clients:
        thread_clients[thread_id] = []
    thread_clients[thread_id].append(request.sid)

@socketio.on("message_sent")
def reload_chat(data):
    print(data)
    thread_id = data['thread_id']
    if thread_id in thread_clients:
        for client_sid in thread_clients[thread_id]:
            socketio.emit(
            "reload_chat", {"threadId": thread_id}, namespace="/", room=client_sid
        )


if __name__ == "__main__":
    socketio.run(app, debug=True)
