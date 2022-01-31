import sqlite3
conn=sqlite3.connect("employees_1.db",check_same_thread=False)
# print("Database opened successfully")
conn.execute("create table employee_tb(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL);")
# print("table created successfully")
conn.execute("alter table employee_tb add email TEXT NOT NULL;")
conn.execute("alter table employee_tb add address TEXT NOT NULL;")
# conn.execute("alter table employee_tb rename to employee_tb;")
# curs=conn.cursor()
name='mani1'
email='abc.com'
address='odc'
def adding_employee_tb(name,email,address):
    with conn:
        curs = conn.cursor()
        curs.execute('INSERT into employee_tb(name,email,address) values(?,?,?);', (name, email, address))
        conn.commit()
        msg = "employee successfully added"
        return msg
adding_employee_tb(name,email,address)