from flask_wtf import Form 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
  first_name = StringField('First name', validators=[DataRequired("please enter")])
  last_name = StringField('Last name', validators=[DataRequired("please enter lastname")])
  email = StringField('Email', validators=[DataRequired("enter it"), Email("please enter your email")])
  password = PasswordField('Password', validators=[DataRequired()])
  submit = SubmitField('Sign up')