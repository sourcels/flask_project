from sqlite3 import *
from flask import Flask, render_template, request, redirect, url_for

def connect_db():
    connect020 = connect("chtoto.db")
    connect020.row_factory = Row
    cursor020 = connect020.cursor()
    cursor020.execute('''CREATE TABLE IF NOT EXISTS chtoto(ID INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(100), years_old INTEGER, gender VARCHAR(100), firstname VARCHAR(100), login VARCHAR(100), password VARCHAR(100))''')

    #cursor020.execute('''INSERT INTO chtoto(name, years_old, gender, firstname, login, password) VALUES ("Vasia", 4905, "pilesos", "Fon Shtorfethafenshtrahh", "tochno_ne_nemec", "qwerasdfzxcv]'/3567")''')
    connect020.commit()
    cursor020.execute('''SELECT * FROM chtoto ''')
    vazhnaa_peremenaa = cursor020.fetchall()
    return connect020

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template("main_page.html")

@app.route('/good_places/')
def good_places():
    return render_template("good_places.html")

@app.route('/imba_parks/')
def imba_parks():
    return render_template("imba_parks.html")

@app.route('/intereni_goroda/')
def intereni_goroda():
    return render_template("intereni_goroda.html")

@app.route('/goroda_zahistniki/')
def goroda_zahistniki():
    return render_template("goroda_zahistniki.html")

@app.route('/user_view')
def user_view():
    connect020 = connect_db()
    cursor020 = connect020.cursor()
    cursor020.execute('''SELECT * FROM chtoto ''')
    vazhnaa_peremenaa = cursor020.fetchall()
    return render_template("user_view.html", users=vazhnaa_peremenaa)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        years_old = request.form.get('years_old')
        gender = request.form.get('gender')
        firstname = request.form.get('firstname')
        login = request.form.get('login')
        password = request.form.get('password')

        connect020 = connect_db()
        cursor020 = connect020.cursor()
        cursor020.execute('''INSERT INTO chtoto(name, years_old, gender, firstname, login, password) VALUES (?,?,?,?,?,?)''', [name, years_old, gender, firstname, login, password])
        connect020.commit()
        return redirect(url_for('main_page'))
    else:
        return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')

        sql = '''SELECT login, password FROM chtoto WHERE (?) = login AND (?) = password'''
        connect020 = connect_db()
        cursor020 = connect020.cursor()
        cursor020.execute(sql, [login, password])
        vazhnaa_peremenaa = cursor020.fetchall()
        print(vazhnaa_peremenaa)
        if vazhnaa_peremenaa == []:
            return redirect(url_for('register'))
        else:
            return redirect(url_for('main_page'))
    else:
        return render_template('login.html')



app.run(debug=True)