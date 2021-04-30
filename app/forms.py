from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class UrlForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    ip_que_deve_ser = StringField('IP QUE DEVE SER', validators=[])
    submit = SubmitField('Cadastrar')