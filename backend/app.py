from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from app_static import consult_static

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)
data = "static"


@app.route('/api', methods=['GET'])
def index():
    return {'name': 'Hello World'}


@app.route('/api/change_data')
@app.route('/api/consult')
def consult(query):
    if (data == "static"):
        consult_static(query)
    else:
        print("consult_twitter")

    return "asdas"


@app.route('/api/create', methods=['POST'])
def create():
    request_data = request.data
    print(request_data)
    return {'201': 'Print Correctly'}


if __name__ == '__main__':
    app.run(debug=True)
