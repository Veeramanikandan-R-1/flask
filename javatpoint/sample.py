from flask import Flask
from flask import url_for,redirect,request,render_template

app=Flask(__name__) #creating flask object

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
@app.route('/login',methods=['POST'])
def login():
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

if __name__=="__main__":
    app.run("127.0.0.1",5000,debug=True) #app.run(host, port, debug, options), give host name as string

