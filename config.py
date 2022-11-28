import os
from dotenv import load_dotenv

project_folder = os.path.expanduser("")  # adjust as appropriate
load_dotenv(os.path.join(project_folder, ".env"))

MAIL_API_KEY = os.getenv("MAIL_API_KEY")
MONGO_URI = os.getenv("MONGO_URI")
print(">>>>>>>>>", type(MONGO_URI))
# MONGO_URI = 'mongodb://127.0.0.1/27017';
MONGO_DATABASE = "testdb"
