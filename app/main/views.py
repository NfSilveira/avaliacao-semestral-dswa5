from flask import Flask, flash, render_template, session, redirect, url_for, current_app
from .. import db
from ..models import User, Role, Teacher, Discipline
from ..email import sendgrid_send_message
from . import main
from .forms import NameForm, TeacherForm
from datetime import datetime
from flask_moment import Moment

app = Flask(__name__)
moment = Moment(app)


@main.route('/', methods=['GET', 'POST'])
def index():
    """form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:

            user_role = Role.query.filter_by(name='User').first()

            if user_role is None:
                user_role = Role(name='User')
                db.session.add(user_role)
                db.session.commit()

            user = User(username=form.name.data, role=user_role)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
            print('FLASKY_ADMIN: ' + str(current_app.config['FLASKY_ADMIN']), flush=True)
            if current_app.config['FLASKY_ADMIN']:
                #send_email(current_app.config['FLASKY_ADMIN'], 'New User', 'mail/new_user', user=user)
                print('Enviando mensagem...', flush=True)
                sendgrid_send_message([str(current_app.config['FLASKY_ADMIN']), "flaskaulasweb@zohomail.com"], '[Flask App] Novo Usuário Cadastrado', form.name.data)
                print('Mensagem enviada...', flush=True)
        else:

            if user.role is None:
                user_role = Role.query.filter_by(name='User').first()

                if user_role is None:
                    user_role = Role(name='User')
                    db.session.add(user_role)
                    db.session.commit()

                user.role = user_role
                db.session.commit()

            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('.index'))

    users = User.query.all()
    roles = Role.query.all()

    return render_template('index.html',
                           form=form, name=session.get('name'),
                           known=session.get('known', False), users=users, roles=roles)"""

    return render_template('index.html', current_time=datetime.utcnow())


@main.route('/professores', methods=['GET', 'POST'])
def teachers_page():

    discipline_choices = dict([
        ('dswa5', 'DSWA5'),
        ('gpsa5', 'GPSA5'),
        ('ihca5', 'IHCA5'),
        ('soda5', 'SODA5'),
        ('pjia5', 'PJIA5'),
        ('tcoa5', 'TCOA5'),
    ])

    teacher_registering_form = TeacherForm()
    if teacher_registering_form.validate_on_submit():

        teacher_name=teacher_registering_form.teacherName.data

        teacher = Teacher.query.filter_by(teacher_name=teacher_name).first()
        discipline = teacher_registering_form.discipline.data

        print(f"Teacher Name: {teacher_name}", flush=True)
        print(f"Discipline Name: {discipline}", flush=True)

        if teacher is None:

            teacher_discipline = Discipline.query.filter_by(name=discipline).first()

            if teacher_discipline is None:
                teacher_discipline = Discipline(name=discipline)
                db.session.add(teacher_discipline)
                db.session.commit()
                print(f"New Discipline Created: {teacher_discipline.name}", flush=True)

            print(f"Discipline Assigned: {teacher_discipline.name}", flush=True)

            teacher_discipline = Discipline.query.filter_by(name=discipline).first()

            teacher = Teacher(
                teacher_name=teacher_registering_form.teacherName.data,
                discipline_id=teacher_discipline.id  # Ensure this is set correctly
            )
            db.session.add(teacher)
            db.session.commit()

            flash('Professor cadastrado com sucesso!', 'success')

        else:

            flash('Professor já existe na base de dados!', 'success')

    teachers = Teacher.query.all()
    disciplines = Discipline.query.all()

    return render_template('teachers_page.html', form=teacher_registering_form, teachers=teachers, disciplines=disciplines, discipline_choices=discipline_choices)


@main.route('/disciplinas', methods=['GET'])
def disciplines_page():

    return render_template('whoops.html')


@main.route('/alunos', methods=['GET'])
def students_page():

    return render_template('whoops.html')