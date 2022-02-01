# all crud operation using sqlite3

from flask import Flask
from flask import url_for,redirect,request,render_template,make_response,session,abort,flash
import sqlite3



conn=sqlite3.connect("employees_1.db",check_same_thread=False)

app=Flask(__name__) #creating flask object

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add_employee')
def employee_adding_fun():
    return render_template("add.html")

@app.route('/savedetails',methods=['POST','GET'])
def save_detail_fun():
    if request.method == 'POST':
        msg="msg"
        try:
            name=request.form['name']
            email = request.form['email']
            address = request.form['address']
            # print(name,email,address)
            curs=conn.cursor()
            curs.execute('INSERT into employee_tb(name,email,address) values(?,?,?);', (name,email,address))
            conn.commit()
            msg="employee successfully added"
            # msg=creating_db.adding_employee_tb(name,email,address)

        except Exception as error:
            print(error)
            conn.rollback()
            msg="cannot add employees details"

        finally:
            return render_template('employeed_add_success.html',msg=msg)
            # conn.close()

@app.route('/view_employees')
def viewing_employee_fun():
    with conn:
        conn.row_factory=sqlite3.Row
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM employee_tb')
        rows=cursor.fetchall()
        return render_template('view_employees.html',rows=rows)


@app.route('/delete_entry')
def delete_entry_fun():
    return render_template('delete.html')

@app.route('/delete_record',methods=['POST'])
def deleting_fun():
    try:
        if request.method == "POST":
            name=request.form["name"]
            with conn:
                conn.execute("delete from employee_tb where name=?",(name,))
                msg='record deleted successfully'
    except Exception as error:
        msg='record not deleted'
        print(error)

    finally:
        return render_template('delete_record.html',msg=msg)

if __name__ =="__main__":
    app.run(debug=True)
