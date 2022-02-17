from flask import Flask, jsonify, redirect, url_for, request

app = Flask(__name__)

@app.route('/service',methods = ['POST', 'GET'])
def service_api():
   if request.method == 'POST':
      data = json.loads(request.data)
      text = data.get("text",None)
      if text is None:
         return jsonify({"message":"text not found"})
      else:
         return jsonify(data)
   if request.method == 'GET':
      return "<h1>Welcome to Geeks for Geeks</h1>"
