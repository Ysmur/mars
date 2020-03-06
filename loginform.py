from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, DateField
from wtforms.validators import DataRequired
from datetime import datetime

now = datetime.now()
class LoginForm(FlaskForm):
    email = StringField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')

class JobsForm(FlaskForm):
    team_leader = IntegerField('Руководитель', validators=[DataRequired()])
    job = StringField('Название работы', validators=[DataRequired()])
    work_size = IntegerField('Длительность работы', validators=[DataRequired()])
    collaborators = StringField('Участники', validators=[DataRequired()])
    start_date = DateField('Дата начала', default=now)
    end_date = DateField('Дата окончания', default=now)
    is_finished = BooleanField('Статус', default=False)
    submit = SubmitField('Создать')