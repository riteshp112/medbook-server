import secrets
import hashlib
from operator import itemgetter
from operations import insert


def loginToken(params):
    user = itemgetter("user")(params)
    print(">>>>>>", type(user))
    x = secrets.token_hex(32)
    h = hashlib.new("sha256")
    h.update(x.encode())
    token = h.hexdigest()
    insert({"table": "Tokens", "data": {"user": {"_id": user["_id"]}, "token": token}})
    return {"response": {"result": [{"token": token}]}}
