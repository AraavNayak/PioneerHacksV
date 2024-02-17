from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route("/")
def hello_tinovation():
	return "<h1>Tinovation is so cool</h1>"

if __name__ == "__main__":
	app.run(debug=True, port=5001)