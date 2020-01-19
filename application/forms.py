from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from application.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('An account with that email address already exists. '
                                    + 'Please reset your password or sign up with a different email.')


class ItemForm(FlaskForm):
    material = SelectField(
        'Material',
        choices=[('Glass', 'Glass'), ('Plastic', 'Plastic'), ('Aluminum', 'Aluminum')]
    )
    count = TextAreaField('Count', validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Submit')
