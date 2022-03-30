from flask import Flask, render_template
from lms import app
from lms.forms import Registration



@app.route('/')
def home():
    
    return render_template('index.html')


@app.route('/login')
def login():

    return render_template('login.html')


@app.route('/logininstructor')
def logininstructor():
    return render_template('logininstructor.html')


@app.route('/register')
def register():
    form = Registration()
    return render_template('register.html',form = form)




@app.route('/registerinstructor')
def registerinstructor():
    return render_template('registerinstructor.html')

