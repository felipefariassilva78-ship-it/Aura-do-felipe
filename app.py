from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Gag de la Gag</h1>"

app.run(debug=True, host="0.0.0.0", port=10000)
