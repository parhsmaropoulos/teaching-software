from flask import Flask, render_template, request
from flask_cors import CORS

from models.tests import create_test, get_tests, Question
from models.users import create_user,get_users

app = Flask(__name__)
CORS(app)
@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "GET":
        pass
    
    if request.method == "POST":
        name = request.form.get("name")
        lastname = request.form.get('lastname')
        email = request.form.get("email")
        create_user(name, lastname, email)

    users = get_users()
    return render_template('index.html', users = users)

# @app.route('/question', methods= ['GET', 'POST'])
# def question():
#     if request.method == "GET":
#         pass
#     if request.method == "POST":
#         num1 = request.form.get("num1")
#         num2 = request.form.get("num2")
#         ans = request.form.get("ans")
#         question = {num1, num2, ans}
#         questions.append(question)

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