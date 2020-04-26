from flask import Flask, render_template, request, Response
from flask_cors import CORS, cross_origin
from flask_bcrypt import Bcrypt
import json

from models.tests import create_test, get_tests, Question
from models.users import create_user, get_users, login_user

app = Flask(__name__)
bcrypt = Bcrypt(app)
CORS(app)

@app.route('/users')
def resp():
    response = Response()
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.data = get_users()
    return response

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "GET":
        pass
    
    if request.method == "POST":
        name = request.form.get("name")
        lastname = request.form.get('lastname')
        username = request.form.get('username')
        password = request.form.get('password')
        pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        age = request.form.get('age')
        email = request.form.get("email")
        error = create_user(name, lastname, username, pw_hash, age, email)
        if error != "":
            print(error)
    users = get_users()
    # return render_template('index.html', users = users)
    return users

@app.route('/login', methods= ['GET', 'POST'])
def login():
    if request.method == "GET":
        pass
    if request.method == "POST":
        email = request.form.get('logemail')
        password = request.form.get('logpassword')
        msg, logged_in = login_user(email, password)
        if logged_in:
            tests = get_tests()
            return render_template('dashboard.html', msg = msg, tests = tests)
        return render_template('login.html', msg = msg)
    return render_template('index.html')
        

@app.route('/test', methods=['GET', 'POST'])
def test():
    questions = []
    if request.method == "GET":
        pass
    if request.method == "POST":
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        ans = request.form.get("answer")
        q = Question(Number_1 = num1, Number_2 = num2,Answer = ans)
        questions.append(q)

        teacher_name = request.form.get("teacher_name")
        test_name = request.form.get("test_name")
        create_test(teacher_name, test_name, questions)

    tests = get_tests()
    return render_template('tests.html', tests = tests)

if __name__ == '__main__':
    app.run(debug=True)