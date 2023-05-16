from .Schema import User
from flask import request, Blueprint

user = Blueprint("user",__name__)


@user.route("<get_users>", methods=["GET"])
def get_users():
    users = User.objects.all()
    result = []
    for user in users:
        result.append({"username": user.username})
    return {"result": result}


@user.route("<create_user>", methods=["POST"])
def create_user():
    username = request.json["username"]
    password = request.json["password"]
    name = request.json["name"]
    email = request.json["email"]
    mobile_number = request.json["mobile_number"]
    dob = request.json["dob"]
    gender = request.json["gender"]
    new_user = User(
        username=username,
        password=password,
        name=name,
        email=email,
        mobile_number=mobile_number,
        dob=dob,
        gender=gender,
    )
    new_user.save()
    return {"result": "User created successfully"}
