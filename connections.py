import pymongo
from config import MONGO_URI
client = pymongo.MongoClient(
        MONGO_URI,
        connect=False,
    )
