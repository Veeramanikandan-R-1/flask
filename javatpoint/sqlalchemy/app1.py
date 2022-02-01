from flask import Flask,request,flash,url_for,redirect,render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///employees.sqlite3'
app.config['SECRET_KEY']="secret"

db=SQLAlchemy(app)

class Employees(db.Model):
    id=db.Column('employee_id',db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    email=db.Column(db.String(100))
    address = db.Column(db.String(200))

    def __init__(self,name,email,address):
        self.name=name
        self.email=email
        self.address=address

@app.route('/')
def list_employees():
    return render_template('add.html')

@app.route('/savedetails',methods=['POST',"GET"])
def add_employee():
    if request.method=="POST":
        if not request.form['name'] or not request.form['email'] or not request.form['address']:
            flash('Please enter all the fields','error')
        else:
            employee=Employees(request.form['name'],request.form['email'],request.form['address'])
            db.session.add(employee)
            db.session.commit()
            flash('record was added successfully')
    return render_template('add.html')

@app.route('/listemployees')
def view_all():
    return render_template('view_employees.html',rows=Employees.query.all())

if __name__=="__main__":
    db.create_all()
    app.run(debug=True)