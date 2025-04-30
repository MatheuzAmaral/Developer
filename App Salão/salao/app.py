import sqlite3
def init_db():
    conn = sqlite3.connect('scheduler.db')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS appointments(
          id INTEGER PRIMARY KEY,
          client TEXT,
          date TEXT,
          time TEXT
        )
    ''')
    conn.close()
init_db()

from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TimeField, SubmitField
from wtforms.validators import DataRequired

class AppointmentForm(FlaskForm):
    client = StringField('Nome do Cliente', validators=[DataRequired()])
    date = DateField('Data', validators=[DataRequired()])
    time = TimeField('Horário', validators=[DataRequired()])
    submit = SubmitField('Agendar')

    from flask import render_template, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin

# Configuração
app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua_chave_secreta'
login = LoginManager(app)
login.login_view = 'login'

# Dummy User
class User(UserMixin): id = 1

# Rota de Login
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        login_user(User())
        return redirect(url_for('index'))
    return render_template('login.html')

# Rota Principal
@app.route('/', methods=['GET','POST'])
@login_required
def index():
    form = AppointmentForm()
    if form.validate_on_submit():
        conn = sqlite3.connect('scheduler.db')
        conn.execute(
          'INSERT INTO appointments(client,date,time) VALUES (?,?,?)',
          (form.client.data, form.date.data.isoformat(), form.time.data.isoformat())
        )
        conn.commit(); conn.close()
        flash('Agendamento criado!')
        return redirect(url_for('index'))
    conn = sqlite3.connect('scheduler.db')
    appts = conn.execute('SELECT client,date,time FROM appointments ORDER BY date,time').fetchall()
    conn.close()
    return render_template('index.html', form=form, appointments=appts)

# Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))