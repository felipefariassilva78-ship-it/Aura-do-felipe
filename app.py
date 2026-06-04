from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>The soul eater </h1>
    <h2> Personagems </h2>
    <h2> Maka Albarn </h2>
    <p>Maka Albarn (マカ・アルバーン, Maka Arubān) é a protagonista da série. Ela é uma jovem artesã determinada e corajosa, que tem como objetivo se tornar uma Death Scythe para proteger o mundo dos perigos que o ameaçam. Maka é conhecida por sua inteligência, habilidades de combate e forte senso de justiça. Ela é a parceira de Soul Eater, um garoto que pode se transformar em uma foice, e juntos eles enfrentam diversos desafios e inimigos enquanto buscam alcançar seus objetivos.</p> 
    <img src="https://i.pinimg.com/736x/8f/e4/5e/8fe45e2f720fe42b47243d3264ae71e1.jpg" alt="Maka Albarn" width="300" height="300">
    <h2> Soul Eater </h2>
    <p>Soul Eater (ソウルイーター, Sōru Ītā) é o parceiro de Maka Albarn e um garoto que pode se transformar em uma foice. Ele é um personagem carismático e leal, que tem um forte vínculo com Maka. Soul Eater é conhecido por sua personalidade descontraída e seu estilo de luta único, utilizando suas habilidades de transformação para enfrentar os inimigos. Ele é um dos personagens principais da série e desempenha um papel crucial na jornada de Maka para se tornar uma Death Scythe.</p> 
    <img src="https://i.pinimg.com/1200x/0d/94/4a/0d944a0ca56ba87a07914290838506ad.jpg" alt="Soul Eater" width="300" height="300">
    <p>Death the Kid (デス・ザ・キッド, Desu Za Kiddo) é um dos personagens principais da série. Ele é o filho do Shinigami e um artesão talentoso, conhecido por sua obsessão por simetria. Death the Kid é um personagem carismático e excêntrico, que tem uma personalidade única e um estilo de luta distinto. Ele é parceiro de suas armas, os irmãos Thompson, que podem se transformar em pistolas gêmeas. Juntos, eles enfrentam diversos desafios e inimigos enquanto buscam alcançar seus objetivos.</p>
    <img src="https://i.pinimg.com/736x/07/7d/6f/077d6ff6eed5db3d79269ad47b8fb856.jpg" alt="Death the Kid" width="300" height="300">
    <p>Soul Eater (ソウルイーター, Sōru Ītā) conta a história de uma escola fictícia chamada Shibusen, localizada no estado americano de Nevada, criada para eliminar os ovos de Kishins, que são seres devoradores de almas humanas para se tornarem mais poderosos, e as Bruxas, que vivem aterrorizando o mundo. Os encarregados de eliminar esses seres são os artesãos, que além de eliminar os Kishins, devem ajudar suas armas a se tornarem Death Scythes, para o Shinigami usar como sua própria arma. Os artesãos devem fazer suas armas devorarem 99 ovos de Kishin e uma alma de bruxa para serem Death Scythes. O protagonista da série é Maka Albarn, uma jovem artesã que tem como arma o seu parceiro Soul Eater, um garoto que pode se transformar em uma foice. Juntos, eles enfrentam diversos desafios e inimigos enquanto buscam se tornar Death Scythes e proteger o mundo dos perigos que o ameaçam.</p>
    <a href="https://souleater.fandom.com/pt-br/wiki/Soul_Eater_Wiki">Soul Eater Wiki</a>
    <style>
    p {
    color: White;
    }
        body { 
        background-color: gray;
        background-image: url('https://i.pinimg.com/736x/e4/a6/a6/e4a6a695f93c4c61bef0dc501f4425b4.jpg');
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        <p> {color: White; 
      }  h1 { color: White; }
      h2 { color: White; }
     
    </style>
 <button onclick="document.getElementById('musica').src += '&autoplay=1'">
    Abertura de Soul Eater
  <button onclick="document.getElementById('musica').contentWindow.postMessage('{&quot;event&quot;:&quot;command&quot;,&quot;func&quot;:&quot;stopVideo&quot;,&quot;args&quot;:&quot;&quot;}', '*')">
    Parar a música
</button>

<iframe id="musica" width="0" height="0" 
src="https://www.youtube.com/embed/C_y09j8KPA8?loop=1&enablejsapi=1" 
allow="autoplay">
</iframe>

       """

app.run(debug=True, host="0.0.0.0", port=10000)
