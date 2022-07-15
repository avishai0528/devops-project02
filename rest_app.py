import db_connector
from datetime import datetime
from flask import Flask, request
import os
import signal

now = datetime.now()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

app = Flask(__name__)

# local users storage
users = {}


# supported methods
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'GET':
        try:
            # request_data = request.json
            check_id = db_connector.mysql.check_userid(user_id)
            user_name = db_connector.mysql.select(user_id)
            return {'status': 'ok', 'user_name': user_name}, 200  # status code
        # else:
        except:
            return {'status': 'error', 'reason': 'no such id'}, 500  # status code

    elif request.method == 'POST':
        try:
            # getting the json data payload from request
            request_data = request.json
            # treating request_data as a dictionary to get a specific value from key
            user_name = request_data.get('user_name')
            users[user_id] = user_name
            print(user_id, user_name, formatted_date)
            db_connector.mysql.post(user_id, user_name, formatted_date)
            return {'status': 'ok', 'user_added': user_name}, 200  # status code
        except:
            return {'status': 'error', 'reason': 'id already exists'}, 500  # status code

    elif request.method == 'PUT':
        try:
            # getting the json data payload from request
            request_data = request.json
            # treating request_data as a dictionary to get a specific value from key
            user_name = request_data.get('user_name')
            users[user_id] = user_name
            check_id = db_connector.mysql.check_userid(user_id)
            db_connector.mysql.update(user_id, user_name)
            return {'status': 'ok', 'user_updated': user_name}, 200  # status code
        except:
            return {'status': 'error', 'reason': 'no such id'}, 500  # status code

    elif request.method == 'DELETE':
        try:
            check_id = db_connector.mysql.check_userid(user_id)
            db_connector.mysql.delete_user(user_id)
            return {'status': 'ok', 'user_deleted': user_id}
        except:
            return {'status': 'error', 'reason': 'no such id'}

@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'

app.run(host='127.0.0.1', debug=True, port=5000)
