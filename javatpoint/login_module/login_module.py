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

@app.route('/success',methods=['post','get'])
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
        return render_template('login_retry.html')

@app.route('/logout')
def logout():
    if 'email' in session:
        session.pop("email",None) #mentioned as none to avoid error if email key doesn't exists
        return render_template('logout.html')
    else:
        return 'user already logged out'

# validating using redirect method
@app.route('/validate',methods=['POST'])
def validate():
    if request.method=="POST" and request.form["pass"]=="mani":
        return redirect(url_for("success"))
    return redirect(url_for("login"))

if __name__=="__main__":
    app.run("127.0.0.1",5000,debug=True)