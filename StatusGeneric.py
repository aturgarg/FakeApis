from flask import Flask, json
from flask_api import status
from argparse import ArgumentParser

api = Flask(__name__)

@api.route('/api/<entity>', methods=['GET'])
def response(entity):
    content = {'Message': api.config['content'] or "Error"}
    return content, api.config.get('code')
   
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-code')
    parser.add_argument('-content')
    args = parser.parse_args()    
    api.config['code'] = args.code 
    api.config['content'] = args.content
    api.run()

