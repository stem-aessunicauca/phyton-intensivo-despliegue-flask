from flask import Flask
 
app = Flask(__name__)
 
@app.route("/")
def home_view():
        return "<h1>Welcome to Geeks for Geeks</h1>"
        
# from flask import Flask, redirect, url_for, request
# app = Flask(__name__)
  
# @app.route('/success/<name>')
# def success(name):
#    return 'welcome %s' % name
  
# @app.route('/login',methods = ['POST', 'GET'])
# def login():
#    if request.method == 'POST':
#       user = request.form['nm']
#       return redirect(url_for('success',name = user))
#    else:
#       user = request.args.get('nm')
#       return redirect(url_for('success',name = user))
  
# if __name__ == '__main__':
#    app.run(debug = True)