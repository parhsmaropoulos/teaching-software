from mongoengine import *
from flask_bcrypt import Bcrypt
import datetime

connect('Teaching_Software')

class User(Document):
    first_name= StringField(required=True, max_length=255)
    last_name= StringField(max_length=50)
    
    username = StringField(max_length=50)
    password = StringField(required=True)

    age = IntField(min_value=6, max_value=12)
    email = EmailField(required=True,unique = True)
    
    created_at = DateTimeField(default= datetime.datetime.utcnow())

def create_user(f , l, u, p, a, e):
    ### Check for mail duplicate ###
    err = 1
    error = ""
    try:
        err = User.objects.get(email = e)
    except:
        err = 0
    if err == 0:
        usr = User(first_name= f, last_name = l, username = u, password = p, age = a, email = e).save()
    else:
        error = "Email already taken"
    return error

def get_users():
    users = []

    for user in User.objects:
        users.append(user)
    return users

def login_user(e, p):
    error = ""
    logged_in = False
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
        error = "User logged in Successfuly" 
    return error, logged_in
    