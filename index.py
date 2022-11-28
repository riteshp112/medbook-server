from collections import defaultdict
from operations import invalidOperation,update,select,insert
from methods.Authenticate import authenticateUser
OPERATIONS = defaultdict(
    lambda: invalidOperation,
    {
        "update": update,
        "select": select,
        "insert": insert,
        "authenticateUser": authenticateUser,
    },
)