from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>☠️ SOUL EATER ☠️</h1>
    <hr>
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
    <h2> Black Star </h2>
    <p>Black Star (ブラック☆スター, Burakku Sutā) é um dos personagens principais da série. Ele é um artesão talentoso e um dos mais poderosos da escola Shibusen. Black Star é conhecido por sua personalidade extrovertida e seu estilo de luta agressivo. Ele é um personagem carismático e confiante, que tem um forte vínculo com seu parceiro, Tsubaki Nakatsukasa, que pode se transformar em várias armas diferentes. Juntos, eles enfrentam diversos desafios e inimigos enquanto buscam alcançar seus objetivos.</p>
    <div style="text-align: center;">
     <img src="https://i.pinimg.com/736x/15/cd/73/15cd7325366938f7b7c069a3dbb330a4.jpg" alt="Black Star" width="200" height="200">
    <img src="https://i.pinimg.com/736x/9a/02/39/9a0239afea33341584aea5f80fbcf718.jpg" alt="Black Star" width="200" height="200">
    <img src="https://i.pinimg.com/736x/e1/ff/c5/e1ffc5491e24efe17d688db96a890d2c.jpg" alt="Black Star" width="200" height="200">
    </div>
    <h2> Tsubaki Nakatsukasa </h2>
    <p>Tsubaki Nakatsukasa (中務 哲子, Nakatsukasa Tsubaki) é um dos personagens principais da série. Ela é a parceira de Black Star e pode se transformar em várias armas diferentes, incluindo uma foice, uma espada e uma lança. Tsubaki é conhecida por sua personalidade calma e seu estilo de luta versátil. Ela é uma personagem carismática e leal, que tem um forte vínculo com seu parceiro, Black Star. Juntos, eles enfrentam diversos desafios e inimigos enquanto buscam alcançar seus objetivos.</p>
           <div style="text-align: center;">
    <img src="https://i.pinimg.com/736x/ce/10/de/ce10dec5cffee9ebcf4350f78aad96da.jpg" alt="Tsubaki Nakatsukasa" width="200" height="200">
    <img src="https://i.pinimg.com/736x/17/1f/28/171f284be1f616060060a0900d15326e.jpg" alt="Tsubaki Nakatsukasa" width="200" height="200">
      <img src="https://i.pinimg.com/1200x/f9/94/0c/f9940cf4be8ddf3e00e88684abcff2f9.jpg" alt="Tsubaki Nakatsukasa" width="200" height="200">
    </div>
         <h2> Shinigami </h2>
    <p>Shinigami (死神, Shinigami) é o diretor da escola Shibusen e o pai de Death the Kid. Ele é um personagem carismático e excêntrico, conhecido por sua aparência distinta, que inclui uma máscara de caveira e um terno elegante. Shinigami é um poderoso artesão e um dos personagens mais importantes da série, desempenhando um papel crucial na história e no desenvolvimento dos personagens principais.</p>
    <div style="text-align: center;">
    <img src="https://i.pinimg.com/736x/02/2e/2e/022e2e917a53a2072ccd4f11dffb1080.jpg" alt="Shinigami" width="200" height="200">
          <img src="https://i.pinimg.com/736x/28/ba/85/28ba8572f94f043507757c379c88785d.jpg" alt="Shinigami" width="200" height="200">
    <img src="https://i.pinimg.com/1200x/f2/2a/41/f22a41e4a3e776c13f7f1cee70fb97d8.jpg" alt="Shinigami" width="200" height="200">
    </div>
    <h2> Crona Gorgon </h2>
    <p>Crona (クロナ, Kurona) é um dos personagens principais da série. Ele é um jovem artesão que tem uma personalidade tímida e insegura, e é o parceiro de Ragnarok, uma arma que pode se transformar em uma espada. Crona é conhecido por sua luta interna com seus próprios medos e inseguranças, e por sua jornada de autodescoberta ao longo da série. Ele é um personagem complexo e interessante, que desempenha um papel importante na história e no desenvolvimento dos personagens principais.</p>
    <div style="text-align: center;">
      <img src="https://i.pinimg.com/736x/f4/a9/b0/f4a9b084c84a2ca128aa269727d4de7a.jpg" alt="Crona Gorgon" width="200" height="200">
    <img src="https://i.pinimg.com/736x/8d/04/ec/8d04ec0c2e205a774a392375edda83a3.jpg" alt="Crona Gorgon" width="200" height="200">
    <img src="https://i.pinimg.com/736x/37/c3/6b/37c36b04a8556dcbba9f669fe55f76eb.jpg" alt="Crona Gorgon" width="200" height="200">
    </div>
       <style>
body {
    background-image: url('https://w.wallhaven.cc/full/4y/wallhaven-4y5kzl.jpg');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;

    color: white;
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
}

h1 {
    color: white;
    font-family: 'Cinzel', serif;
    text-align: center;
    font-size: 50px;
    text-shadow: 0 0 15px red;
}

h2 {
    color: white;
    font-family: 'Cinzel', serif;
    text-shadow: 0 0 10px red;
    border-left: 4px solid red;
    padding-left: 10px;
    margin-top: 40px;
}

p {
    color: white;
    background: rgba(0, 0, 0, 0.6);
    padding: 15px;
    border-radius: 10px;
    line-height: 1.6;
}

a {
    color: #ff4444;
    font-weight: bold;
    text-decoration: none;
}

a:hover {
    color: white;
    text-shadow: 0 0 10px red;
}

img {
    width: 220px;
    height: 220px;
    object-fit: cover;

    border: 3px solid red;
    border-radius: 15px;
    margin: 10px;

    transition: all 0.3s ease;
    box-shadow: 0 0 15px rgba(255, 0, 0, 0.5);
}

img:hover {
    transform: scale(1.08);
    box-shadow: 0 0 25px red;
    border-color: white;
}

button {
    background: #cc0000;
    color: white;
    border: none;
    padding: 12px 20px;
    border-radius: 10px;
    cursor: pointer;
    margin: 10px;
    font-size: 16px;
    transition: 0.3s;
}

button:hover {
    background: #ff0000;
    transform: scale(1.05);
    box-shadow: 0 0 15px red;
}

::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-track {
    background: #111;
}

::-webkit-scrollbar-thumb {
    background: red;
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: #ff3333;
}
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

if __name__ == "__main__":
    app.run(debug=True)

