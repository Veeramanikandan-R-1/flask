from flask_wtf import Form
from flask import Flask,flash,render_template,redirect,url_for
from wtforms import IntegerField,StringField,TextAreaField,SubmitField,RadioField,SelectField
from wtforms import validators,ValidationError

app=Flask(__name__)
app.secret_key="dev_key"

class contact_form(Form):
    name=StringField("Candidate Name",[validators.input_required("Enter name")])
    gender=RadioField('Gender',choices=[('M',"Male"),('F','Female')])
    address=TextAreaField("Address")
    email=StringField("email",[validators.input_required("enter email address"),validators.Email('enter email')])
    age=IntegerField('age')
    language=SelectField('programming lang',choices=[('java','Java'),('py','Python')])
    submit=SubmitField('submit')

@app.route('/contact',methods=['GET','POST'])
def contact():
    form=contact_form()
    if form.validate()==False:
        flash('all fields required')
    return render_template('contact.html',form=form)

@app.route('/success',methods=['POST'])
def success_fun():
    return 'form posted successfully'

if __name__=="__main__":
    app.run(debug=True)

