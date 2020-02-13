import os
from flask import Flask
from flask import render_template
from .forms import AcquisitionForm
import pandas as pd
from wtforms import FloatField
from wtforms.validators import DataRequired
import xlrd
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, '')


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
    def format(x):
        return "${:.1f}K".format(x/1000)

    def format_billion(x):
        return f'${int(x):n}'

    xlsx = pd.ExcelFile('app/asset_perf_summary.xlsx')
    df1_mf = pd.read_excel(xlsx, 'multifamily')
    df2_comm = pd.read_excel(xlsx, 'commercial')

    df1_mf["Occ Date"] = df1_mf["Occ Date"].map(lambda x: datetime(*xlrd.xldate_as_tuple(x, 0)).date())
    df1_mf['Orig Sale Proforma Amt'] = df1_mf['Orig Sale Proforma Amt'].apply(format)

    curr_val_mf = format_billion(df1_mf[' Value Estimate'].sum())
    curr_val_comm = format_billion(df2_comm[' Value Estimate'].sum())

    headers = df1_mf.columns.tolist()
    df_mf = df1_mf.values.tolist()

    return render_template("am_dashboard.html",
                           df_mf=df_mf,
                           headers=headers,
                           curr_val_mf=curr_val_mf,
                           curr_val_comm=curr_val_comm)


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
        setattr(AcquisitionForm, name, FloatField(var, validators=[DataRequired()]))

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
#     return app/