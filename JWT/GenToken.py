import jwt
import jsonify
import datetime
import time
import random


def GenToken():
    token = jwt.encode({'user' : 'rampage', 'exp' : datetime.datetime.utcnow() + datetime.timedelta(seconds=3600)}, 'ourkey')
    return(token)


def BuildNTokens(N):
    """Experimental"""
    for i in range (N):
        token = jwt.encode({'user' : 'rampage', 'exp' : datetime.datetime.utcnow() + datetime.timedelta(seconds=3600)}, 'ourkey')
        print(token)
        print('')

def DecodeToken():

    return(jwt.decode(GenToken(), 'ourkey'))

print(GenToken())
