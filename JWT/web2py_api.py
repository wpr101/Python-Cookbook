import jwt
import datetime
from functools import wraps

SECRET_KEY = 'our_secret'

def index(): 
    return 'hello world'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.vars['token'] #http://localhost:5000/route?token=adsfdafdsaf

        if not token:
            return response.json({'message': 'Token is missing!'})

        try:
            data = jwt.decode(token, SECRET_KEY)
        except:
            return response.json({'message' : 'Token is invalid'})
            
        return f(*args, **kwargs)
    return decorated

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
        return ('You have reached the protected resource')
    except:
        return response.json({'message' : 'Token is invalid'})

@token_required
def protected_v2():
    return('You have reached the protected resource v2')
