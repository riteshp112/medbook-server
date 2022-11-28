from bson import json_util
from bson.objectid import ObjectId
import json 

def parse_json(data):
    return json.loads(json_util.dumps(data))

def parseRequest(object):
    finalObject = {}
    for key in object.keys():
        value = object[key]
        if key == "_id":
            finalObject[key] = ObjectId(value)
        else:
            finalObject[key] = value
    return finalObject
