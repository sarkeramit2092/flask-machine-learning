from flask_wtf import FlaskForm

from wtforms import (
  StringField,
  SelectField,
  DateField,
  PasswordField,
  SubmitField,
  BooleanField
)

from wtforms.validators import (
  DataRequired,
  Length,
  Email,
  Optional,
  EqualTo
)


class SignupForm(FlaskForm):
  username = StringField("Username",
                         validators= [DataRequired(), Length(5, 25)])
  
  email = StringField("Email",
                         validators= [DataRequired(), Email()]) #Email() -under the wood it used email-validator package
  
  gender = SelectField("Gender",
                       choices=["Male", "Female", "Other"],
                       validators= [Optional()])
  
  dob   = DateField ("Date of Birth",
                     validators= [Optional()])
  
  password = PasswordField ("Password",
                            validators=[DataRequired(), Length(5,20)])
  
  confirm_password = PasswordField ("Confirm Password",
                            validators=[DataRequired(), Length(5,20), EqualTo('password')])
  
  submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
  email = StringField("Email",
                      validators= [DataRequired(), Email()])
  
  password = PasswordField ("Password",
                            validators=[DataRequired(), Length(5,20)])
  
  remember_me = BooleanField ("Remember Me")

  submit = SubmitField("Login")
