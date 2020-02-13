import os
from flask import Flask
from flask import render_template
from .forms import AcquisitionForm
import pandas as pd
from wtforms import FloatField
from wtforms.validators import DataRequired


app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
@app.route('/dashboard')
def dashboard():
    """
    ROUTE FOR DASHBOARD
    :return:
    """
    return render_template("template.html")


@app.route('/acquisitions_model')
def acquisitions_model():
    """
    ROUTE FOR MODELING A DEAL
    :return:
    """

    df = pd.read_excel('app/model_fields.xlsx')
    fields = df.values.tolist()
    for field in fields:
        var = field[0]
        name = var.replace(" ", "_")
        setattr(AcquisitionForm, name, FloatField(name, validators=[DataRequired()]))

    acq_form = AcquisitionForm()

    return render_template('acquisitions_model.html', form=acq_form)


# def create_app(test_config=None):
#     # create and configure the app
#     app = Flask(__name__, instance_relative_config=True)
#     # app.config.from_mapping(
#     #     SECRET_KEY='dev',
#     #     DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
#     # )
#
#     if test_config is None:
#         # load the instance config, if it exists, when not testing
#         app.config.from_pyfile('config.py', silent=True)
#     else:
#         # load the test config if passed in
#         app.config.from_mapping(test_config)
#
#     # ensure the instance folder exists
#     try:
#         os.makedirs(app.instance_path)
#     except OSError:
#         pass
#
#     return app