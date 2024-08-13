from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, RadioField

class SignUpForm(FlaskForm):
    username = StringField('Username ')
    email = StringField('Email')
    password = PasswordField('Password')
    birthday = DateField('Date of Birth')
    gender = RadioField('Gender', choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    submit = SubmitField('Sign Up')