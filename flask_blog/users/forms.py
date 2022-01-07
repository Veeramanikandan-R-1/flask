from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flask_blog.models import User


class Registration_form(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # creating validation error function
    # to check whether user already exist in db and maintain unique
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        # if user is none if condition dont execute
        if user:
            raise ValidationError("Username not available, Try different one")

    # to maintain unique email
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        # if user is none if condition dont execute
        if user:
            raise ValidationError("email not available, Try different one")


class Login_form(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    picture = FileField("Update Profile picuture", validators=[FileAllowed(["jpg", "png"])])

    submit = SubmitField('Update')

    # creating validation error function
    # to check whether only new detail are given
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            # if user is none if condition dont execute
            if user:
                raise ValidationError("Username not available, Try different one")

    # to maintain unique email
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            # if user is none if condition dont execute
            if user:
                raise ValidationError("email not available, Try different one")


class RequestResetForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    submit=SubmitField('Send request to the mail')

    # to maintain unique email
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        # if user is none if condition dont execute
        if user is None:
            raise ValidationError("No account with that email, You must register first.")

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')