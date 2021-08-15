from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

emp_data_dict = \
{
  100: {
    "name": "Jhon",
    "designation": "Senior Engineer",
    "salary": "34000"
  },
  200: {
    "name": "Mary",
    "designation": "Software Engineer",
    "salary": "25000"
  }
}

class employee(Resource):

    def get(self, emp_id):
        return emp_data_dict[emp_id]


api.add_resource(employee, '/employee/<int:emp_id>')


if __name__ == '__main__':
    app.run(debug=True)





