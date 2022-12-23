from operator import itemgetter
from operations import select
from bson.objectid import ObjectId


def authenticateUser(params):
    token = itemgetter("token")(params)
    result = select({"table": "Tokens", "condition": {"token": token}, "limit": 1})
    result = result["response"]["result"]
    print(result)
    if len(result):
        result = result[0]
        userId = result["user"]["_id"]
        userDetails = select(
            {"table": "testcol", "condition": {"_id": ObjectId(userId)}, "limit": 1}
        )
        userDetails = userDetails["response"]["result"][0]
        return {"response": {"result": [userDetails]}}
    else:
        return {"error": "You have to login first."}
