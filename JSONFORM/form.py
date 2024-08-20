from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField 

class SignIn(FlaskForm):
    username = StringField('Username ')
    email = StringField('Email')
    password = PasswordField('Password')