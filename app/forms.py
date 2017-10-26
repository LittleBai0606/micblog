from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import Required, DataRequired,Email,Length

class LoginForm(FlaskForm):
    user_name = StringField('user name', validators=[DataRequired(), Length(max=15)])
    remember_me = BooleanField('remember me', default=False)
    submit = SubmitField('Log in')

class SignUpForm(FlaskForm):
    user_name = StringField('user name', validators=[DataRequired(), Length(max=15)])
    user_email = StringField('user email', validators=[Email(), DataRequired(), Length(max=128)])
    submit = SubmitField('Sign up')
