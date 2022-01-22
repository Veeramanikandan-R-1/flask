from flask import Flask
from flask import url_for,redirect,request,render_template,make_response,session,abort,flash

app=Flask(__name__) #creating flask object
app.secret_key='abc'

def welcome_page():
    return "this is welcome page"

@app.route('/home/<string:name>') #to pass variable in decorator, using converter int to accept only int values
def home(name):
    return "hello {}!".format(name); #don't forget to add semicolon

app.add_url_rule("/welcome","welcome",welcome_page) #routing using add url rule

#using url for dynamic url linking
@app.route('/admin')
def admin():
    return 'admin'

@app.route('/manager')
def manager():
    return 'manager'

@app.route('/user/<name>')
def user(name):
    if name=="admin":
        return redirect(url_for('admin'))
    elif name=="manager":
        return redirect(url_for('manager'))

#handling post request from form
@app.route('/login1',methods=['POST'])
def login1():
    uname=request.form['uname']
    password=request.form['pass']
    if uname=="mani" and password=="123":
        return 'Welcome {} !'.format(uname)

#handling get request from form
@app.route('/login_get',methods=['GET'])
def login_get1():
    uname=request.args.get('uname')
    password=request.args.get('pass')
    if uname=="mani" and password=="123":
        return 'Welcome {} !'.format(uname)

#returning tag
@app.route('/h1')
def html_return():
    return "<html><body><h1>mani</h1></body></html>"

#returning external template
@app.route('/')
def render():
    return render_template("message.html")

#using delimiters
@app.route('/delimiter/<name>')
def delimiter(name):
    return render_template("message.html",name=name)

#using delimiter python statements
@app.route('/print_table/<int:num>')
def print_table(num):
    return render_template("table.html",n=num)

#flask request object
@app.route('/customer_add')
def customer_form():
    return render_template('customer.html')

@app.route('/success1',methods=['GET','POST'])
def print_data():
    if request.method=="POST":
        customer_data=request.form
        return render_template('print_customer_data.html',customer_data=customer_data)

@app.route('/cookie')
def cookie():
    res=make_response("<p>cookie is set</p>")
    res.set_cookie("name","mani")
    return res

#creating login module using set cookie
@app.route('/error')
def error():
    return "<p><strong>enter correct password</strong></p>"

@app.route('/login')
def login():
    return render_template("login.html")

@app.route("/success",methods=['POST','GET'])
def success():
    if request.method=="POST":
        email=request.form['email']
        password=request.form['pass']
        # print(password)
    if request.method == "GET":
        flash("you are logged in ")
        # k="mani"
        return redirect(url_for("view_profile"))
    else:
        return redirect(url_for("error"))

@app.route('/viewprofile')
def view_profile():
    k=request.cookies.get("email")
    k="mani" #user when cookies are not set
    # resp=make_response(render_template("profile.html"),k=k)
    return render_template("profile.html",k=k)


#using session for user login
@app.route('/setsession')
def home1():
    res=make_response("<h4>sess var set, <a href='/get'>get var</a></h4>") #dont use "" in href
    session['response']="session#1"
    return res

@app.route('/get')
def get_session():
    if 'response' in session:
        s=session['response']
        return render_template("getsession.html",name=s)

# validating using redirect method
@app.route('/validate',methods=['POST'])
def validate():
    if request.method=="POST" and request.form["pass"]=="mani":
        return redirect(url_for("success"))
    return redirect(url_for("login"))

# using abort function to display errors
@app.route('/abort')
def abort1():
    abort(403)


if __name__=="__main__":
    app.run("127.0.0.1",5000,debug=True) #app.run(host, port, debug, options), give host name as string

