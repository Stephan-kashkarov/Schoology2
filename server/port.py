from app import app, db
from app.models import User, Post, Following

print('\n' + "-" * 25 + "\n Ports server is ONLINE \n" + "-" * 25 + '\n')


@app.shell_context_processor
def make_shell_context():
	return {
		'db': db,
		'User': User,
		'Post': Post,
		'Following': Following
	}
