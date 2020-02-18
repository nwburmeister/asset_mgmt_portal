from flask_wtf import FlaskForm, Form
from wtforms import TextAreaField
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import pandas as pd


class AcquisitionForm(FlaskForm):
    """
    FORM FOR THE ACQUISITIONS MODEL
    """
    submit = SubmitField('Submit')


class YardiForm(FlaskForm):

    property_code = StringField('Property Code', validators=[DataRequired(), Length(min=2, max=20)])
    book_code = StringField('Book Code', validators=[DataRequired(), Length(min=2, max=20)])
    account_tree = StringField('Account Tree', validators=[DataRequired(), Length(min=2, max=20)])

    period_start = StringField('Period Start', validators=[DataRequired(), Length(min=2, max=20)])
    period_end = StringField('Period End', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Pull Data')
