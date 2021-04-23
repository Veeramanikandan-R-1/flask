from flask import Flask
app=Flask("__name__")
@app.route('/kalam/')
def print():
   return '<h1>mani</h1>'
@app.route('/home')
def home():
   return 'home'
if __name__=='__main__':
   app.run(debug=True,port=6365)