# from flask_wtf import Form
# from wtforms import StringField, PasswordField, SubmitField
# from wtforms.validators import DataRequired

# class SignUpForm(Form):
#     first_name = StringField('First Name', validators=[DataRequired])
#     last_name = StringField('Last Name', validators=[DataRequired])
#     email = StringField('Email', validators=[DataRequired])
#     password = PasswordField('Password', validators=[DataRequired])
#     submit = SubmitField('Sign Up', validators=[DataRequired])


from flask_wtf import Form 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignUpForm(Form):
  first_name = StringField('First name', validators=[DataRequired("Please enter your first name.")])
  last_name = StringField('Last name', validators=[DataRequired("Please enter your last name.")])
  email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Enter your correct email")])
  password = PasswordField('Password', validators=[DataRequired("Please enter a password."), Length(min=6, message="Length must be at least 6 characters")])
  submit = SubmitField('Sign up')