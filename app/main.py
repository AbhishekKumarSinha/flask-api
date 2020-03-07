import json
import logging

from flask import Flask, session, redirect, url_for, request, jsonify, make_response

from app import users

flaskapp = Flask(__name__)

@flaskapp.route('/test', methods=['GET'])
def test():
    if request.method == 'GET':
        return "Test"

@flaskapp.route('/totalusers', methods=['GET'])
def total_users():
    if request.method == 'GET':
        content_type = request.headers.get('Content-type')
        if content_type == "application/json":
            total = users.total_users()
            print(total)
            response_obj = {
                'status' : 'Success',
                'message' : 'Total Users : ' + str(total)
            }
            return make_response(jsonify(response_obj)), 200

@flaskapp.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        content_type = request.headers.get('Content-type')
        if content_type == "application/json":
            if request.is_json:
                recvd_json = request.get_json()
                recvd_username = recvd_json['username']
                recvd_password = recvd_json['password']
                try:
                    if users.registered_users[recvd_username] == recvd_password:
                        users.user_status[recvd_username] = True
                        response_obj = {
                            'status' : 'Success',
                            'message' : 'Login Success!'
                        }
                        return make_response(jsonify(response_obj)), 200
                    else:
                        response_obj = {
                            'status' : 'Fail',
                            'message' : 'Login Failed!'
                        }
                        return make_response(jsonify(response_obj)), 404
                except:
                    response_obj = {
                            'status' : 'Fail',
                            'message' : 'Login Failed!'
                    }
                    return make_response(jsonify(response_obj)), 404

@flaskapp.route('/logout', methods=['POST'])
def logout():
    if request.method == 'POST':
        content_type = request.headers.get('Content-type')
        if content_type == "application/json":
            if request.is_json:
                recvd_json = request.get_json()
                recvd_username = recvd_json['username']
                if users.user_status[recvd_username] == True:
                    users.user_status[recvd_username] = False
                    response_obj = {
                        'status' : 'Success',
                        'message' : 'Logout Success!'
                    }
                    return make_response(jsonify(response_obj)), 200
                else:
                    response_obj = {
                        'status' : 'Fail',
                        'message' : 'Logout Failed!'
                    }
                    return make_response(jsonify(response_obj)), 404

@flaskapp.route('/deposit', methods=['POST'])
def deposit():
    if request.method == 'POST':
        content_type = request.headers.get('Content-type')
        if content_type == "application/json":
            if request.is_json:
                recvd_json = request.get_json()
                recvd_username = recvd_json['username']
                amount = recvd_json['amount']
                if users.user_status[recvd_username] is True:
                    if recvd_username in users.user_account:
                        users.user_account[recvd_username] = users.user_account[recvd_username] + amount
                    else:
                        users.user_account[recvd_username] = amount
                    response_obj = {
                        'status' : 'Success',
                        'message' : 'Amount Deposited!'
                    }
                    return make_response(jsonify(response_obj)), 200
                else:
                    response_obj = {
                            'status' : 'Fail',
                            'message' : 'Please Login!'
                    }
                    return make_response(jsonify(response_obj)), 400

@flaskapp.route('/balance', methods=['GET'])
def balance():
    if request.method == 'GET':
        content_type = request.headers.get('Content-type')
        if content_type == "application/json":
            if request.is_json:
                recvd_json = request.get_json()
                recvd_username = recvd_json['username']
                if recvd_username in users.user_account:
                    amount = users.user_account[recvd_username]
                    response_obj = {
                    'status' : 'Success',
                    'message' : 'Amount : ' + amount
                    }
                    return make_response(jsonify(response_obj)), 200
                else:
                    response_obj = {
                        'status' : 'Fail',
                        'message' : 'No User Account!'
                    }
                    return make_response(jsonify(response_obj)), 404

@flaskapp.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        content_type = request.headers.get('Content-type')
        if content_type == "application/json":
            if request.is_json:
                recvd_json = request.get_json()
                recvd_username = recvd_json['username']
                recvd_password = recvd_json['password']

                users.registered_users[recvd_username] = recvd_password
                users.user_status[recvd_username] = False
                response_obj = {
                    'status' : 'Success',
                    'message' : 'Account Created!'
                }
                return make_response(jsonify(response_obj)), 201


def main():
    flaskapp.run()

if __name__ == "__main__":
    main()