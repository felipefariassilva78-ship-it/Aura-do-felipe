from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>The soul eater </h1>
    <p>Soul Eater (ソウルイーター, Sōru Ītā) conta a história de uma escola fictícia chamada Shibusen, localizada no estado americano de Nevada, criada para eliminar os ovos de Kishins, que são seres devoradores de almas humanas para se tornarem mais poderosos, e as Bruxas, que vivem aterrorizando o mundo. Os encarregados de eliminar esses seres são os artesãos, que além de eliminar os Kishins, devem ajudar suas armas a se tornarem Death Scythes, para o Shinigami usar como sua própria arma. Os artesãos devem fazer suas armas devorarem 99 ovos de Kishin e uma alma de bruxa para serem Death Scythes. O protagonista da série é Maka Albarn, uma jovem artesã que tem como arma o seu parceiro Soul Eater, um garoto que pode se transformar em uma foice. Juntos, eles enfrentam diversos desafios e inimigos enquanto buscam se tornar Death Scythes e proteger o mundo dos perigos que o ameaçam.</p>
    <img src="https://i.pinimg.com/1200x/15/d2/54/15d25459b7bfa3564137569a73ef4b40.jpg" style="position: center;">
    <a href="https://souleater.fandom.com/pt-br/wiki/Soul_Eater_Wiki">Soul Eater Wiki</a>
    <style>
        body { 
        background-color: gray;
        background-image: url('https://i.pinimg.com/736x/2a/ea/89/2aea89eabcab76bd190aab015e6ab66a.jpg');
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
      }  h1 { color: Black; }
    </style>
 <button onclick="document.getElementById('musica').src += '&autoplay=1'">
    Abertura de Soul Eater
</button>

<iframe id="musica" width="0" height="0" 
src="https://www.youtube.com/embed/C_y09j8KPA8?loop=1" 
allow="autoplay">
</iframe>

       """

app.run(debug=True, host="0.0.0.0", port=10000)
