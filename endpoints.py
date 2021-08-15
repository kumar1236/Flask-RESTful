from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

eng_emp_data_dict = \
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

sales_emp_data_dict = \
{
  500: {
    "name": "Emiley",
    "designation": "VP, sales",
    "salary": "123000"
  },
  600: {
    "name": "Joseph",
    "designation": "Field Sales Engineer",
    "salary": "125000"
  }
}

class Engineeringemployee(Resource):

    def get(self, emp_id):
        return eng_emp_data_dict[emp_id]

class Salesemployee(Resource):

    def get(self, emp_id):
        return sales_emp_data_dict[emp_id]


#api.add_resource(Engineeringemployee, '/engineering_employee/<int:emp_id>', '/engg/<int:emp_id>')
#api.add_resource(Salesemployee, '/sales_employee/<int:emp_id>', '/sales/<int:emp_id>')

# Example for endpoints when multiple add_resource are required
api.add_resource(Engineeringemployee, '/engineering_employee/<int:emp_id>', endpoint='engg_1')
api.add_resource(Engineeringemployee, '/engg/<int:emp_id>', endpoint='engg_2')


if __name__ == '__main__':
    app.run(debug=True)





