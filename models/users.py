from mongoengine import *
from flask_bcrypt import Bcrypt
from .grades import Grade, FinalGrade
from bson import ObjectId
import datetime
import json

connect('Teaching_Software')

class User(Document):
    first_name= StringField(required=True, max_length=255)
    last_name= StringField(max_length=50)
    
    username = StringField(max_length=50, unique = True)
    password = StringField(required=True)

    age = IntField(min_value=6, max_value=12)
    email = EmailField(required=True,unique = True)
    authenticated = BooleanField(default=False)

    type = StringField(required=True)
    photo = ImageField(thumbnail_size=(150,150, False))
    
    created_at = DateTimeField(default= datetime.datetime.utcnow())
    
    
def get_user_by_user_id(_id):
    user = User.objects.get(id = _id)
    return user

def create_user(f , l, u, p, a, e, t, phot):
    ### Check for mail duplicate ###
    err = 1
    error = ""
    try:
        err = User.objects.get(email = e)
    except:
        err = 0
    if err == 0:
        usr = User(first_name= f, last_name = l, username = u, password = p, age = a, email = e, type=t, photo = phot).save()
    else:
        error = "Email already taken"
    return error

def get_users():
    users = []
    for user in User.objects:
        users.append(user)
    return users

    # q_set = User.objects()
    # json_users = q_set.to_json()
    # return json_users

def login_user(e, p):
    error = ""
    logged_in = False
    id = 0
    user_type = ""
    user_id = 0
    ### Check for email ###
    try:
        usr = User.objects.get(email = e)
    except:
        error = "Email does not exist!"
        return error
    ### Check for password match ###
    if error == "":
        if (Bcrypt.check_password_hash('', usr.password, p)):
            error = ""
            logged_in = True
        else:
            error = "Password does not match!"
    if error == "":
        user_type = usr.type
        user_id = str(usr.id)
        error = "User logged in Successfuly" 
    return (error, logged_in, user_type, user_id)
    
def update_user(u, a, f, l, e, _id):
    user = User.objects(id = _id).update(
        first_name = f,
        last_name = l,
        username = u,
        age = a,
        email = e
    )
    return user

def get_test_results(username):
    ids = {}
    grades = Grade.objects(username=username)
    for grade in grades:
        id = ObjectId(grade.test_id)
        ids[id] = grade.grade
    return ids