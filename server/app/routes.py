from app import app
from flask import request


@app.route("/")
@app.route("/hello", methods=['GET', 'POST'])
def hello():
	try:
		if request.form["string"]:
			string = request.from["string"]
		else:
			string = 'Hello, World!'
	except:
		abort(400)
	return string
