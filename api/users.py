import hashlib
from .mongo import users
from flask import Blueprint, request
from .utils import send_otp, verify_otp


usersBlueprint = Blueprint('auth', __name__)


@usersBlueprint.route("/register", methods=['POST'])
def registerUser():
    user = request.get_json()
    pwd = hashlib.sha256(user['password'].encode('utf-8')).hexdigest()
    query = {
        'password': pwd,
        'email': user['email'],
        'username': user['username'],
        'phone': user['phone'],
        'role': 'user'
    }
    users.insert_one(query)
    return query

@usersBlueprint.route('/login', methods=['POST'])
def login():
    user = request.get_json()
    query = {
        "email": user['identifier'] 
    }
    user_found = users.find_one(query)
    if user_found == None:
        return 'User credentials wrong!!'
    
    user_found["_id"] = str(user_found["_id"])
    pwd = hashlib.sha256(user['password'].encode('utf-8')).hexdigest()
    
    if pwd == user_found['password']:
        return (send_otp('+16412339280'))
    
    return 'User credentials wrong!!'


@usersBlueprint.route('/verify-otp', methods=['POST'])
def verify_user_otp():
    request_body = request.get_json()
    otp = request_body['otp']
    receiver = request_body['receiver']
    # return jsonify({
    #     'num': receiver,
    #     'code': otp
    # })
    return verify_otp(receiver, otp)

