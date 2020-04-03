from flask import Flask, json
from flask_api import status
from argparse import ArgumentParser

api = Flask(__name__)

@api.route('/api/<entity>', methods=['GET'])
def response(entity):
    content = {'Issue': 'there is an error'}
    return content, api.config.get('code')

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-a')
    args = parser.parse_args()
    val = args.a
    api.config['code'] = val    
    api.run()

