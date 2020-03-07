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
                recv_username = recvd_json['username']
                recv_password = recvd_json['password']
                try:
                    if users.registered_users[recv_username] == recv_password:
                        users.user_status[recv_username] = True
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
                recv_username = recvd_json['username']
                if users.user_status[recv_username] == True:
                    users.user_status[recv_username] = False
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


@flaskapp.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        content_type = request.headers.get('Content-type')
        if content_type == "application/json":
            if request.is_json:
                recvd_json = request.get_json()
                recv_username = recvd_json['username']
                recv_password = recvd_json['password']

                users.registered_users[recv_username] = recv_password
                users.user_status[recv_username] = False
                response_obj = {
                    'status' : 'Success',
                    'message' : 'Account Created!'
                }
                return make_response(jsonify(response_obj)), 201


def main():
    flaskapp.run()

if __name__ == "__main__":
    main()