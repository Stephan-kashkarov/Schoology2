from app import app


@app.route("/")
@app.route("/hello")
def hello():
	return "hello, world!"
