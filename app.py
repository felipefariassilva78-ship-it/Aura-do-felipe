from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Caras maneiros nunca traem</h1>
    <img src="https://i.pinimg.com/1200x/15/d2/54/15d25459b7bfa3564137569a73ef4b40.jpg">
    <input type="text">
    """

app.run(debug=True, host="0.0.0.0", port=10000)
