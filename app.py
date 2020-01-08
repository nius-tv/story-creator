from flask import Flask, request


app = Flask(__name__)


@app.route('/stories', methods=['POST'])
def add_story():
	data = request.get_json()
	print(data)
