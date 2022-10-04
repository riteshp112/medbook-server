import pymongo
from config import MONGO_DATABASE, MONGO_URI
client = pymongo.MongoClient(
        MONGO_URI,
        connect=False,
    )
db=client[MONGO_DATABASE]
