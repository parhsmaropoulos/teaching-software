from mongoengine import *
import datetime
import json

connect('Teaching_Software')

class Question(EmbeddedDocument):
    Number_1 = IntField(min_value=0,max_value=10)
    Number_2 = IntField(min_value=0,max_value=10)
    Answer = IntField(required= True)

class Test(Document):
    Teacher = StringField(max_length=50, required= True)
    Test_Name = StringField(max_length= 50)
    For_Number = IntField(min_value=0, max_value=10)
    Questions = EmbeddedDocumentListField(Question)
    Final = BooleanField()
    Created_At = DateTimeField(default= datetime.datetime.utcnow())


def create_test(data):
    questions = []
    for question in data['data']:
        q = Question(Number_1 = question['f'], Number_2 = question['s'], Answer = question['a'])
        questions.append(q)
    if (data['final'] == 'Simple Test'):
        Final = False
    else:
        Final =True;
    test = Test(Teacher = data['teacher_name'], Test_Name = data['test_name'],Final = Final, Questions = questions, For_Number = data['for_number']).save()
    return test
        
def get_tests():
    tests = []
    for test in Test.objects:
        if (test.Final != True):
            tests.append(test)
    return tests

def get_final_tests():
    final_tests = []
    for test in Test.objects():
        if test.Final:
            final_tests.append(test)
    return final_tests

def get_tests_by_teacher(teacher_name):
    tests = []
    get_tests = Test.objects(Teacher = teacher_name)
    for test in get_tests:
        tests.append(test)
    return tests
def get_test_by_id(_id):
    test = Test.objects.get(id = _id)
    return test

def calculate_grade(_id, answer):
    i = 0;
    correct = 0;
    test = Test.objects.get(id = _id)
    for question in test.Questions:
        if question.Answer == int(answer[i]):
            correct = correct + 1
        i += 1
    grade = (correct*10)/ i
    grade = round(grade,1)
    return grade, correct