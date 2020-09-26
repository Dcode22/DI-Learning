import flask
from school import app

@app.route("/")
def index():
	return "Working..."

@app.route("/students")
def get_students():

	# Model
	# get students from Database

	# View
	render template

	return "There are no Students"