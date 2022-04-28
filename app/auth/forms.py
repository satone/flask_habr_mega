from flask_babel import lazy_gettext as _l, _
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo

from app.models import User


class LoginForm(FlaskForm):
    username = StringField(_l('User'), validators=[DataRequired()])
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    remember_me = BooleanField(_l('Remember me'))
    submit = SubmitField(_l('Login'))


class RegistrationForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    email = StringField(_l('Email'), validators=[Email()])
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    password2 = PasswordField(_l('Retype password'), validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_l('Register'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_('Please enter another name'))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_('Please use another email'))


class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    submit = SubmitField(_l('Request Password Reset'))


class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    password2 = PasswordField(_l('Repeat password'), validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_l('Request Password Reset'))
