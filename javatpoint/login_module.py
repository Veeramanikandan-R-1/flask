from flask import Flask
from flask import url_for,redirect,request,render_template,make_response,session

app=Flask(__name__) #creating flask object
app.secret_key='abc'

# login logout session management

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/success',methods=['post'])
def success():
    if request.method=="POST":
        session['email']=request.form['email']
    return render_template("success.html")

@app.route('/profile')
def profile():
    if 'email' in session:
        email=session['email']
        return render_template('profile.html',k=email)
    else:
        return 'please login first'

@app.route('/logout')
def logout():
    if 'email' in session:
        session.pop("email",None) #mentioned as none to avoid error if email key doesn't exists
        return render_template('logout.html')
    else:
        return 'user already logged out'

if __name__=="__main__":
    app.run("127.0.0.1",5000,debug=True)