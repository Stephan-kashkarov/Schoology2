from app import app


@app.route("/")
@app.route("/hello", methods=['GET', 'POST'])
def hello():
	if request.form["string"]:
		string = request.from["string"]
	else:
		string = 'Hello, World!'
	return string
