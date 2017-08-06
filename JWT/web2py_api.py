import jwt
import datetime

SECRET_KEY = 'our_secret'

def index(): 
    return 'hello world'

def get_token():
    token = jwt.encode({'user' : 'rampage', 'exp' : datetime.datetime.utcnow() + datetime.timedelta(seconds=3600)}, SECRET_KEY)
    return response.json({'token' : token})

def unprotected():
    return response.json({'message' : 'This is an unprotected resource'})

def protected():
    token = request.vars['token']
    if not token:
        return response.json({'message' : 'The token is missing'})

    try:
        data = jwt.decode(token, SECRET_KEY)
        return ('You have reached the promised land')
    except:
        return response.json({'message' : 'Token is invalid'})
    
