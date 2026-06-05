from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>The soul eater </h1>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel&display=swap" rel="stylesheet">
    <p>Soul Eater (ソウルイーター, Sōru Ītā) conta a história de uma escola fictícia chamada Shibusen, localizada no estado americano de Nevada, criada para eliminar os ovos de Kishins, que são seres devoradores de almas humanas para se tornarem mais poderosos, e as Bruxas, que vivem aterrorizando o mundo. Os encarregados de eliminar esses seres são os artesãos, que além de eliminar os Kishins, devem ajudar suas armas a se tornarem Death Scythes, para o Shinigami usar como sua própria arma. Os artesãos devem fazer suas armas devorarem 99 ovos de Kishin e uma alma de bruxa para serem Death Scythes. O protagonista da série é Maka Albarn, uma jovem artesã que tem como arma o seu parceiro Soul Eater, um garoto que pode se transformar em uma foice. Juntos, eles enfrentam diversos desafios e inimigos enquanto buscam se tornar Death Scythes e proteger o mundo dos perigos que o ameaçam.</p>
    <a href="https://souleater.fandom.com/pt-br/wiki/Soul_Eater_Wiki" target="_blank">Soul Eater Wiki</a>
    <h2> Personagems </h2>
    <h2> Maka Albarn </h2>
    <p>Maka Albarn (マカ・アルバーン, Maka Arubān) é a protagonista da série. Ela é uma jovem artesã determinada e corajosa, que tem como objetivo se tornar uma Death Scythe para proteger o mundo dos perigos que o ameaçam. Maka é conhecida por sua inteligência, habilidades de combate e forte senso de justiça. Ela é a parceira de Soul Eater, um garoto que pode se transformar em uma foice, e juntos eles enfrentam diversos desafios e inimigos enquanto buscam alcançar seus objetivos.</p> 
      <div style="text-align: center;">
      <img src="https://i.pinimg.com/736x/8f/e4/5e/8fe45e2f720fe42b47243d3264ae71e1.jpg" alt="Maka Albarn" width="200" height="200">
    <img src="https://i.pinimg.com/736x/76/f0/05/76f005727de802c7091820e7e3bebcfb.jpg" alt="Maka Albarn" width="200" height="200">
     <img src="https://i.pinimg.com/736x/67/84/e7/6784e77b9f97e8bddb99584d91ab6f86.jpg" alt="Maka Albarn" width="200" height="200">
    </div>
    <h2> Soul Eater </h2>
       <p>Soul Eater (ソウルイーター, Sōru Ītā) é o parceiro de Maka Albarn e um garoto que pode se transformar em uma foice. Ele é um personagem carismático e leal, que tem um forte vínculo com Maka. Soul Eater é conhecido por sua personalidade descontraída e seu estilo de luta único, utilizando suas habilidades de transformação para enfrentar os inimigos. Ele é um dos personagens principais da série e desempenha um papel crucial na jornada de Maka para se tornar uma Death Scythe.</p> 
    <div style="text-align: center;"> 
       <img src="https://i.pinimg.com/1200x/0d/94/4a/0d944a0ca56ba87a07914290838506ad.jpg" alt="Soul Eater" width="200" height="200">
    <img src="https://i.pinimg.com/736x/cb/89/fc/cb89fc8d0e1efef830c9af9f4a64ac68.jpg" alt="Soul Eater" width="200" height="200">
    <img src="https://i.pinimg.com/736x/d6/20/4c/d6204c06dc751c6a8b6c4de2fd775feb.jpg" alt="Soul Eater" width="200" height="200">
    </div>
      <h2> Death the Kid </h2>
    <p>Death the Kid (デス・ザ・キッド, Desu Za Kiddo) é um dos personagens principais da série. Ele é o filho do Shinigami e um artesão talentoso, conhecido por sua obsessão por simetria. Death the Kid é um personagem carismático e excêntrico, que tem uma personalidade única e um estilo de luta distinto. Ele é parceiro de suas armas, os irmãos Thompson, que podem se transformar em pistolas gêmeas. Juntos, eles enfrentam diversos desafios e inimigos enquanto buscam alcançar seus objetivos.</p>
     <div style="text-align: center;">
         <img src="https://i.pinimg.com/736x/07/7d/6f/077d6ff6eed5db3d79269ad47b8fb856.jpg" alt="Death the Kid" width="200" height="200">
    <img src="https://i.pinimg.com/736x/3a/ed/1a/3aed1a3f90390189b14851b702fb018b.jpg" alt="Death the Kid" width="200" height="200">
    <img src="https://i.pinimg.com/736x/57/da/15/57da15bc1a74965070828e25a666a095.jpg" alt="Death the Kid" width="200" height="200">
      </div>   
   <h2> Patricia Thompson </h2>
    <p>Patricia Thompson (パトリシア・トンプソン, Patorishia Tompuson) é um dos personagens principais da série. Ela é uma das armas gêmeas de Death the Kid e pode se transformar em uma pistola. Patricia é conhecida por sua personalidade extrovertida e seu estilo de luta agressivo. Ela é uma personagem carismática e leal, que tem um forte vínculo com seu parceiro, Death the Kid. Juntos, eles enfrentam diversos desafios e inimigos enquanto buscam alcançar seus objetivos.</p>
    <div style="text-align: center;">
    <img src="https://i.pinimg.com/736x/b8/ec/82/b8ec82b7434c4b0d0cb89abf0897df0e.jpg" alt="Patricia Thompson" width="200" height="200">
    <img src="https://i.pinimg.com/736x/15/a4/d5/15a4d5cb058a583abe1b83badc75bd0c.jpg" alt="Patricia Thompson" width="200" height="200">
    <img src="https://i.pinimg.com/736x/98/9f/4d/989f4d83bf919ae7891bda0004e87ee7.jpg" alt="Patricia Thompson" width="200" height="200">
    </div>
    <h2> Liz Thompson </h2>
    <p>Liz Thompson (リズ・トンプソン, Rizu Tompuson) é um dos personagens principais da série. Ela é a irmã gêmea de Patricia Thompson e também pode se transformar em uma pistola. Liz é conhecida por sua personalidade calma e seu estilo de luta preciso. Ela é uma personagem carismática e leal, que tem um forte vínculo com seu parceiro, Death the Kid. Juntos, eles enfrentam diversos desafios e inimigos enquanto buscam alcançar seus objetivos.</p>
    <div style="text-align: center;">
    <img src="https://i.pinimg.com/1200x/e1/8a/1c/e18a1c3d157a27de33ccc5a90bf42cda.jpg" alt="Liz Thompson" width="200" height="200">
    <img src="https://i.pinimg.com/736x/e2/47/c6/e247c6a742b3bcc10f08e7c486420eae.jpg" alt="Liz Thompson" width="200" height="200">
    <img src="https://i.pinimg.com/736x/d1/65/08/d165084a1271bb713929ad5456c36d79.jpg" alt="Liz Thompson" width="200" height="200">
    </div>
  
     
       <style>
    img: hover {
    opacity: 0.7;
    }
    p {
    color: White;
    }
        body { 
        background-image: url('https://w.wallhaven.cc/full/4y/wallhaven-4y5kzl.jpg');
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        } 
       h1 {color: White !important; font-family: 'Cinzel', serif;} 
      h2 { color: White !important; font-family: 'Cinzel', serif;}
     
    </style>
<button onclick="document.getElementById('musica').src += '&autoplay=1'">
    Abertura de Soul Eater
</button>

<button onclick="document.getElementById('musica').contentWindow.postMessage('{&quot;event&quot;:&quot;command&quot;,&quot;func&quot;:&quot;stopVideo&quot;,&quot;args&quot;:&quot;&quot;}', '*')">
    Parar a música
</button>

<iframe id="musica" width="0" height="0" 
src="https://www.youtube.com/embed/C_y09j8KPA8?loop=1&enablejsapi=1" 
allow="autoplay">
</iframe>

       """

app.run(debug=True, host="0.0.0.0", port=10000)
