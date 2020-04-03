from flask import Flask, json
from flask_api import status

api = Flask(__name__)

@api.route('/api/<entity>', methods=['GET'])
def response(entity):
    content = {'Issue': 'there is an error'}
    return content, status.HTTP_401_UNAUTHORIZED

if __name__ == '__main__':
    api.run()

