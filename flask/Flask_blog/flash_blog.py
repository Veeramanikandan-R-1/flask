from flask import Flask, render_template, url_for, flash, redirect
from form import Registration_form,Login_form
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__) #__name__ is the name of the module

# secret key
app.config['SECRET_KEY']='67e30547f37df0b4bfd158ab4deee457'

posts=[
    {
        'author':'mani',
        'title':'blog spot 1',
        'content':'first content',
        'date_posted':'17th apr 2021'
    },
{
        'author':'harish',
        'title':'blog spot 2',
        'content':'second content',
        'date_posted':'16th apr 2021'
    }
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='about')

@app.route("/register",methods=['GET','POST'])
def register():
    form = Registration_form() #creating instance
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data} !','success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    form = Login_form() #creating instance
    if form.validate_on_submit():
        if form.email.data=='admin@blog.com' and form.password.data=='password':
            flash('You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash('invalid credential please check username or password','danger ')
    return render_template('login.html', title='login', form=form)

if __name__=="__main__":
    app.run(debug=True)