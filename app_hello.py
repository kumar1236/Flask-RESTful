from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello World!'}

    def post(self):
        return {'message': 'This is a response for POST request!'}

    def put(self):
        return {'message': 'This is a response for PUT request!'}

    def delete(self):
        return {'message': 'This is a response for DELETE request!'}

class HelloWorld1(Resource):
    def get(self, name):
        return {'message': 'Hello! ' + name}

class HelloWorld2(Resource):
    def get(self, name1, name2):
        return {'message': 'Hello! ' + name1 + " and " + name2}

api.add_resource(HelloWorld, '/greeting')
api.add_resource(HelloWorld1, '/greeting/<string:name>')
api.add_resource(HelloWorld2, '/greeting/<string:name1>/<string:name2>')



if __name__ == '__main__':
    app.run(debug=True)





