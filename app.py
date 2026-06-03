from flask import Flask        # 1. Importa o Flask

app = Flask(__name__)          # 2. Cria o site

@app.route("/")                # 3. Define o endereço da página
def home():                    # 4. Função que roda quando acessar
    return "<h1>Gag de la Gag </h1>"    # 5. O que aparece na página

app.run(debug=True)            # 6. Liga o servidor