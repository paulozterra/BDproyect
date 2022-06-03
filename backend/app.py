from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)


@app.route('/api', methods=['GET'])
def index():
    return {'name': 'Hello World'}


@app.route('/api/create', methods=['POST'])
def create():
    request_data = request.data
    print(request_data)
    return {'201': 'Print Correctly'}


if __name__ == '__main__':
    app.run(debug=True)
