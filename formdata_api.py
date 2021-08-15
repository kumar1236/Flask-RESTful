from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

book_details = {}

class Book(Resource):

    def get(self, book_id):
        if book_id in book_details:
            return book_details[book_id]
        return {'message': 'Book with id ' + book_id + ' not found'}

    def post(self, book_id):
        if book_id in book_details:
            return {'message': 'Book with id ' + book_id + ' already exists'}
        
        print("Request body contents " + str(request.form))
        return {'message': 'Book with id ' + book_id + ' added'}

api.add_resource(Book, '/books/<string:book_id>')

if __name__ == '__main__':
    app.run(debug=True)





