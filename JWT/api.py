from flask import Flask, jsonify, request, make_response
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisthesecretkey'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token') #http://localhost:5000/route?token=adsfdafdsaf

        if not token:
            return jsonify({'message': 'Token is missing!'}), 403

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message' : 'Token is invalid'}), 403
            
        return f(*args, **kwargs)
    return decorated

@app.route('/unprotected')
def unprotected():
    return jsonify({'message' : 'Anyone can view this!'})

@app.route('/protected')
@token_required
def protected():
    return jsonify({'message' : 'This is only available for people with valid tokens.'})

#to get the token
@app.route('/login')
def login():
    auth = request.authorization

    if auth and auth.password == 'secret2':
        token = jwt.encode({'user' : auth.username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(seconds=3600)}, app.config['SECRET_KEY'])
        return jsonify({'token' : token})
    return (make_response('Could not verify!', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'}))

if __name__ == '__main__':
    app.run(debug=True)
