from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Caras maneiros nunca traem</h1>
    <img src="https://i.pinimg.com/1200x/15/d2/54/15d25459b7bfa3564137569a73ef4b40.jpg">
    <input type="text">
    <a href="https://souleater.fandom.com/pt-br/wiki/Soul_Eater_Wiki">Soul Eater Wiki</a>
    <style>
        body { background-color: black;
      }  h1 { color: white; }
    </style>
    """

app.run(debug=True, host="0.0.0.0", port=10000)
