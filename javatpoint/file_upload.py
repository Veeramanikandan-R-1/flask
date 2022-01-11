from flask import Flask
from flask import url_for,redirect,request,render_template,make_response,session

app=Flask(__name__) #creating flask object
app.secret_key='abc'

@app.route('/')
def upload():
    return render_template("file_upload_form.html")

@app.route('/success_file',methods=['POST'])
def file_upload_success():
    if request.method=="POST":
        f=request.files['file']
        f.save("D:\\mani\\2\\flask\\flask1\\javatpoint\\uploaded_files\\"+f.filename) #to save a file to particular folder
    return render_template('file_success.html',name=f.filename)
#ds
if __name__=="__main__":
    app.run("127.0.0.1",5000,debug=True) #app.run(host, port, debug, options), give host name as string