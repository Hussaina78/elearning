from flask import Flask, render_template
from lms import app
from lms.forms import Registration,Login



@app.route('/')
def home():
    
    return render_template('index.html')



@app.route('/logininstructor')
def logininstructor():
    return render_template('logininstructor.html')


@app.route('/register', methods=['GET' ,'POST'])
def register():
    form = Registration()
    if form.validate_on_submit():
        print("hello world")
        #..return redirect(url_for('.index'))
    return render_template('register.html',form = form)
    

@app.route('/login')
def login():
    form = Login()
    return render_template('login.html',form = form)




@app.route('/registerinstructor')
def registerinstructor():
    return render_template('registerinstructor.html')

