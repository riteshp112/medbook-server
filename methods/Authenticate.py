from operator import itemgetter
from operations import select


def authenticateUser(params):
    token = itemgetter("token")(params)
    result = select({"table": "Tokens", "condition": {"token": token}})
    if len(result):
        result = result[0]
        userId = result.user._id
        userDetails = select({"table": "testcol", "condition": {"_id": userId}})
        return {result: userDetails}
    else:
        return {"error": "You have to login first."}
