from mongoengine import *
import datetime

connect('TeachingSoftware')

class Question(EmbeddedDocument):
    Number_1 = IntField(min_value=0,max_value=10)
    Number_2 = IntField(min_value=0,max_value=10)
    Answer = IntField(required= True)

class Test(Document):
    Teacher = StringField(max_length=50, required= True)
    Test_Name = StringField(max_length= 50)
    Questions = EmbeddedDocumentListField(Question)
    Created_At = DateTimeField(default= datetime.datetime.utcnow())

def create_test(t, n, list):
    questions = []
    for i in list:
        question = {i.Number_1,i.Number_2,i.Answer}
        questions.append(question)
    test =Test(Teacher = t, Test_Name =  n, Questions = list).save()
        
def get_tests():
    tests = []
    for test in Test.objects:
        tests.append(test)
    return tests
