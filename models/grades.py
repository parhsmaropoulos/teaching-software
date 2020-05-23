from mongoengine import *
from bson import ObjectId

connect('Teaching_Software')

class Grade(Document):
    username = StringField(required=True)
    test_id = StringField()
    grade_for_number_test = IntField(min=1, max =10)
    grade = FloatField(min=0, max=10, required=True)

class FinalGrade(Document):
    username = StringField(required=True)
    test_id = StringField()
    grade = FloatField(min=0, max=10, required=True)


def insert_grade(u, g, f, num, _id):
    if f == True:
        grade = FinalGrade(username = u, grade = g ,test_id = _id).save()
    else:
        grade = Grade(username = u, grade = g, grade_for_number_test = num,test_id = _id).save()

def get_grades_by_username(f, u):
    if f == False:
        grades = Grade.objects(username = u)
    if f == True:
        grades = FinalGrade.objects(username = u)
    return grades

def get_top_grades_per_test(u):
    max_grades ={}
    grades = Grade.objects(username = u)
    for grade in grades:
        id = ObjectId(grade.test_id)
        if id in max_grades:
            if max_grades[id] < grade.grade:
                max_grades[id] = grade.grade
        else:
            max_grades[id] = grade.grade
    return max_grades

def get_grades_percentages_per_username_per_test(u):
    grade_percentages = {}
    grades = Grade.objects(username = u)
    for grade in grades:
        g = grade.grade * 10
        for_num = grade.grade_for_number_test
        if for_num in grade_percentages:
            prev = grade_percentages.get(for_num)
            grade_percentages[for_num] = (prev+g)/2
        else:
            grade_percentages[for_num] = g
    return grade_percentages

