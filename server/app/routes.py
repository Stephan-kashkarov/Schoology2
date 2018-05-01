from app import app
from flask import request, abort


@app.route("/")
@app.route("/hello", methods=['GET', 'POST'])
def hello():
	try:
		if request.form["string"]:
			form = request.form
			string = form["string"]
		else:
			string = 'Hello, World!'
	except:
		abort(400)
	return string


@app.route("/profile", methods=["POST"])
def username():
	pass


@app.route("")
def pass_hash():
	pass
