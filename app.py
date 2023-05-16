from flask import Flask
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from modules.user.Routes import user

app = Flask(__name__)
CORS(app)
app.register_blueprint(user)
app.config['MONGODB_SETTINGS'] = {
    'db': 'mydatabase',
    'host': 'mongodb://localhost:27017/mydatabase'
}
db = MongoEngine(app)



if __name__ == "__main__":
    app.run(debug=True)
