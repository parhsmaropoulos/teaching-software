from mongoengine import *
import datetime
connect('TeachingSoftware')

class User(Document):
    first_name= StringField(required=True, max_length=255)
    last_name= StringField(max_length=50)
    email = EmailField(required=True,unique = True)
    created_at = DateTimeField(default= datetime.datetime.utcnow())

def create_user(f , l, e):
    usr = User(first_name= f, last_name = l, email = e).save()

def get_users():
    users = []

    for user in User.objects:
        users.append(user)
    return users

