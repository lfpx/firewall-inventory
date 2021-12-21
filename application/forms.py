from flask_wtf import FlaskForm
from flask_wtf import FlaskForm
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class HostForm(FlaskForm):
    host_name = StringField("Hostname", validators=[DataRequired()])
    host_ip = StringField("IP", validators=[DataRequired()])
    submit = SubmitField("Add Host")