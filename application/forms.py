from flask_wtf import FlaskForm
from flask_wtf import FlaskForm
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired

# Host form
class HostForm(FlaskForm):
    host_name = StringField("Hostname", validators=[DataRequired()])
    host_ip = StringField("IP", validators=[DataRequired()])
    submit = SubmitField()

# Rule form
class RuleForm(FlaskForm):
    port = IntegerField("Port", validators=[DataRequired()])
    allow = BooleanField("Allow")
    submit = SubmitField()