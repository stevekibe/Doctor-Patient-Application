from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError,BooleanField
from wtfforms.validators import Required,Email,EqualTo
from ..models import PatientUser

class RegistrationForm(FlaskForm):
    email = StringField('your email address', validators=[Required(),Email()])
    username = StringField('your username', validators=[Required()])
    Password = PasswordField('password', validators=[Required(),EqualTo('password', message='passwords must match')])
    password_confirm = PasswordField('confirm password',validators=[Required()])
    submit = SubmitField('sign Up')

    #validators for username and email
    def validate_email(self,data_field):
        #function that validates the emails

        if PatientUser.query.filter_by(email= data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        #function that validates the username

        if PatientUser.query.filter_by(username= data_field.data).first():
            raise ValidationError('Username already taken')

class LoginForm(FlaskForm):
    email = StringField('Your email address', validators=[Required(),Email()])
    password = PasswordField('password', validators=[Required()])
    remeber = BooleanField('remeber me')
    submit = SubmitField('Sign in')
     

        


