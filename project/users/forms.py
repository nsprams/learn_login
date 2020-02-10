# project/users/forms.py
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtfomr.validators import DataRequired, Length, EqualTo, Email


class RegistrationForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=40)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=4-)])
    confirm = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])

