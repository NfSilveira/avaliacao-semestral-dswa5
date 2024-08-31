from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

class TeacherForm(FlaskForm):

    teacherName = StringField('Cadastre o novo professor:', validators=[DataRequired()])
    discipline = SelectField(u'Disciplina associada:', choices=[('dswa5', 'DSWA5'), ('gpsa5', 'GPSA5'), ('ihca5', 'IHCA5'), ('soda5', 'SODA5'), ('pjia5', 'PJIA5'), ('tcoa5', 'TCOA5'), ])
    submit = SubmitField('Cadastrar')