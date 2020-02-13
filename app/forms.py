from flask_wtf import FlaskForm, Form
from wtforms import TextAreaField
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import pandas as pd


class AcquisitionForm(FlaskForm):
    """
    FORM FOR THE ACQUISITIONS MODEL
    """