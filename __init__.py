from flask import Flask, render_template, request, Response, session, make_response, redirect, g , url_for, send_file
from flask_cors import CORS, cross_origin
from flask_bcrypt import Bcrypt
from flask_assets import Environment, Bundle

from IPython.display import Image
from functools import  wraps
from mongoengine import *


import json
import io
import numpy as np

from models.tests import create_test, get_tests, Question, get_tests_by_teacher, get_test_by_id,  calculate_grade
from models.users import create_user, get_users, login_user, get_user_by_user_id, update_user, get_test_results
from models.grades import insert_grade, get_grades_by_username, get_grades_percentages_per_username_per_test

app = Flask(__name__)
assets = Environment(app)
connect(db="Teaching_Software")

style_bundle = Bundle(
    'css/*.css',
    output='dist/css/style.min.css',
    extra={'rel': 'stylesheet/css'}
)

sass_bundle = Bundle(
    'sass/*.scss',
    'sass/lbd/*.scss',
    output='dist/sass/style.min.scss'
)
js_bundle = Bundle('js/core/jquery.3.2.1.min.js',
                    'js/core/popper.min.js',
                    'js/core/bootstrap.min.js',
                    'js/plugins/*.js',
                    'js/light-bootstrap-dashboard.js',
                    output='dist/js/main.min.js',
                    extra={'rel': 'text/javascript'})
assets.register('main_js', js_bundle)
assets.register('main_scss', sass_bundle)
assets.register('main_styles', style_bundle)
style_bundle.build()
sass_bundle.build()
js_bundle.build()


bcrypt = Bcrypt(app)

CORS(app)


# def login_required(f):
#     @wraps(f)
#     def decorated_funtion(*args, **kwargs):
#         if g.user is None:
#             return redirect(url_for('index', next=request.url))
#         return f(*args, **kwargs)
#     return decorated_funtion


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "GET":
        users = get_users()
        return render_template('index.html')
        # return users   

@app.route('/login', methods= ['GET', 'POST'])
def login():
    if request.method == "GET":
        pass
    if request.method == "POST":
        session.pop('user_id', None)
        session.pop('user_type', None)

        email = request.form.get('logemail')
        password = request.form.get('logpassword')
        msg, logged_in, user_type, user_id = login_user(email, password)
        print(user_type, user_id)
        if logged_in:
            session['user_type'] = user_type
            session['user_id'] = user_id
            return render_template('dashboard.html', msg = msg, session = session)
        return render_template('login.html', msg = msg)
    return render_template('index.html')     

@app.route('/logout', methods = ['GET'])
def logout():
    session.clear()
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
        name = request.form.get("name")
        lastname = request.form.get('lastname')
        username = request.form.get('username')
        password = request.form.get('password')
        photo = request.files['photo']
        pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        age = request.form.get('age')
        email = request.form.get("email")
        type = request.form.get("type")
        error = create_user(name, lastname, username, pw_hash, age, email, type, photo)
        if error != "":
            print(error)
        return render_template('index.html')



@app.route('/users')
def resp():
    users = get_users()
    return render_template('users.html', users = users)

@app.route('/userslist-user/<string:id>')
def get_userlist_user(id):
    user = get_user_by_user_id(id)
    grades = get_grades_by_username(False, user.username)
    final_grades = get_grades_by_username(True, user.username)
    grades_perc = get_grades_percentages_per_username_per_test(user.username)
    print(grades_perc)
    return render_template('userlist-user.html', user = user, grades = grades, grades_perc = grades_perc, finals = final_grades)


@app.route('/user/<string:id>', methods=['GET'])
def get_user_by_id(id):
    user =  get_user_by_user_id(id)
    grades = get_grades_by_username(False, user.username)
    final_grades = get_grades_by_username(True, user.username)
    grades_perc = get_grades_percentages_per_username_per_test(user.username)
    print(grades)
    return render_template('user.html', user = user,grades = grades, grades_perc = grades_perc, finals = final_grades)

@app.route('/update_profile/<string:id>', methods=['POST'])
def update_user_by_id(id):
    username  = request.form.get('username')
    age  = request.form.get('age')
    first_name  = request.form.get('first_name')
    last_name  = request.form.get('last_name')
    email  = request.form.get('email')
    user = update_user(username, age, first_name, last_name, email, id)
    return redirect(url_for('get_user_by_id', id=id))

@app.route('/show/<string:id>')
def show_image(id):
    user = get_user_by_user_id(id)
    return send_file(user.photo, as_attachment=True, attachment_filename='profileImage.png')

@app.route('/dashboard')
def dashboard():
    user_id = session['user_id']
    user = get_user_by_user_id(user_id)
    grades_perc = get_grades_percentages_per_username_per_test(user.username)
    print(grades_perc)
    return render_template('dashboard.html', grades_perc = grades_perc)
        
@app.route('/pushgrade', methods=['POST'])
def pushgrade():
    grade = request.form.get('grade')
    username = request.form.get('username')
    number = request.form.get('for_number')
    final = request.form.get('final')
    print(number)
    if final == 'f':
        final = False
    else:
        final = True
    insert_grade(username, grade, final, number)
    return render_template('index.html')

@app.route('/tests', methods=['GET', 'POST'])
def tests():
    if request.method == "GET":
        user_id = session['user_id']
        user_type = session['user_type']
        user = get_user_by_user_id(user_id)
        tests = get_tests()
        ids = get_test_results( user.username)
        print(ids)
        return render_template('tests.html', tests = tests, ids = ids)

@app.route('/create_test', methods=['GET', 'POST'])
def create_test_form():
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        json_data = request.get_json()
        print(json_data)
        test = create_test(json_data)
        print(test)
        pass
    return render_template('create_test.html')

@app.route('/tests/<string:name>', methods=['GET', 'POST'])
def get_tests_by_teacher_name(name):
    if request.method == "GET":
        response = Response()
        response.headers["Access-Control-Allow-Origin"] = "*"
        tests = get_tests_by_teacher(name)
    return render_template('tests.html', tests = tests)

@app.route('/test/<string:id>', methods=['GET'])
def get_test_by_test_id(id):
    if request.method == "GET":
        test = get_test_by_id(id)
    return render_template('test.html', test = test)

@app.route('/start_test/<string:id>', methods=['POST', 'GET'])
def start_test(id):
    if request.method == "GET":
        test = get_test_by_id(id)
        return render_template('start_test.html', test = test)
    if request.method == "POST":
        # post answers
        return render_template('completed_test.html')

@app.route('/submit_results', methods =['POST'])
def submit_res():
    answers = request.form.getlist('answer')
    test_id = request.form.get('test_id')
    test = get_test_by_id(test_id)
    for_number = test.For_Number
    final = test.Final
    # Calculate the grade
    grade, correct = calculate_grade(test_id, answers)
    # Get user attrs
    user_id = session['user_id']
    user = get_user_by_user_id(user_id)
    username = user.username
    insert_grade(username, grade, final, for_number, test_id)

    return render_template('completed_test.html', grade= grade, correct= correct, user=user)

@app.route('/number_wiki/<int:number>')
def wiki_number(number):
    return render_template('wiki_number.html', number= number)

if __name__ == '__main__':
    app.secret_key = b'\x11\x00e\x90\x93{\xb5\x15?\x97Q\xce\xf3\xe1\xffc'
    app.run(debug=True)