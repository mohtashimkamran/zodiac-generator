import json
from utils.translations import Texts
# generates server error response 
# use-case : sql-query execution
def generateServerErrorResponse():
    response = {
        "statusCode": "",
        "errorCode" : 500,
        "errorMessage": "Internal Server Error"
    }
    return response,500

def generateClientErrorResponse(errorCode, errorMsg):
    response = {
        "statusCode": "",
        "errorCode" : errorCode,
        "errorMessage" :  errorMsg,
    }
    return response

def generateServerStatusResponse(statusCode):
    response = {
        "statusCode": statusCode,
        "errorCode": "",
        "errorMessage": "",
    }
    return response
    

def PlusParentuneResponseError(errorCode, errorMsg,lang='en'):
    res = {
        "statusCode": errorCode,
        "message": Texts(errorMsg,lang),
        "data": {},
        "error": [
            {
                "error_code": errorMsg,
                "data": {}
            }
            ]
    }
    return res

def PlusParentuneResponse(status, msg, data):
    response = {
        "statusCode": status,
        "message": msg,
        "data":data,
        "error":[]
        }
    return response