from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField ,BooleanField
from wtforms.validators import DataRequired,Length, EqualTo
from wtforms.validators import Email

class Registration_form(FlaskForm):
    username= StringField('Username', validators=[DataRequired(),Length(min=2,max=20)])
    email= StringField('E-mail', validators=[DataRequired(), Email()])
    password= PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit= SubmitField('Sign Up')

class Login_form(FlaskForm):
    email= StringField('E-mail', validators=[DataRequired(), Email()])
    password= PasswordField('Password', validators=[DataRequired()])
    remember= BooleanField('Remember me')
    submit= SubmitField('Login')