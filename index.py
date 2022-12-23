from collections import defaultdict
from operations import invalidOperation, update, select, insert
from methods.Authenticate import authenticateUser
from methods.Login import loginToken

OPERATIONS = defaultdict(
    lambda: invalidOperation,
    {
        "update": update,
        "select": select,
        "insert": insert,
        "loginToken": loginToken,
        "authenticateUser": authenticateUser,
    },
)
