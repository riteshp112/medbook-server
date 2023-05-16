from app import db
class User(db.Document):
    name=db.StringField(required=True)
    username = db.StringField(required=True)
    password = db.StringField(required=True)
    email = db.EmailField(required=True)
    mobile_number = db.StringField(required=True)
    dob=db.DateField(required=True)
    gender=db.StringField(required=True)
    otp=db.IntField()
