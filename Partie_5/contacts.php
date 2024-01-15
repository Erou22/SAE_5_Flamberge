<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <title>Contacts</title>
  <link rel="stylesheet" type="text/css" href="style.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>

<body>
  <?php require("./header.php") ?>

  <main>

    <h1>Contacts</h1>

    <aside class="presentation">
      <p>Nous sommes 3 étudiants (précédemment <span id="valerian">4</span>) en 3ème année en BUT Informatique à l'IUT de Lannion.</p>
      <br>
      <p>Pour la SAÉ 5C, il nous a fallu réaliser un système de recommandation de films, et celui-ci est intégré à ce
        site par le biais d'une API.</p>
      <hr>
      <p>Vous pouvez nous contacter par mail ou sur Discord, avec les liens suivants :</p>
    </aside>

    <article>
      <h2>Erwan FERTRAY</h2>
      <a href="mailto:erwan.fertray@etudiant.univ-rennes1.fr"><i class="fa fa-envelope"></i>erwan.fertray@etudiant.univ-rennes1.fr</a>
      <br>
      <a href="https://discord.com/users/429370662612631552" target="_blank" rel="noopener noreferrer"><i class="fa-brands fa-discord"></i>erou22</a>
      <hr>
    </article>

    <article>
      <h2>Evan CARADEC</h2>
      <a href="mailto:evan.caradec@etudiant.univ-rennes1.fr"><i class="fa fa-envelope"></i>evan.caradec@etudiant.univ-rennes1.fr</a>
      <br>
      <a href="https://discord.com/users/299951419417427978" target="_blank" rel="noopener noreferrer"><i class="fa-brands fa-discord"></i>liebherru</a>
      <hr>
    </article>

    <article>
      <h2>Mathéo ALLAIN</h2>
      <a href="mailto:matheo.allain@etudiant.univ-rennes1.fr"><i class="fa fa-envelope"></i>matheo.allain@etudiant.univ-rennes1.fr</a>
      <br>
      <a href="https://discord.com/users/213310416103800832" target="_blank" rel="noopener noreferrer"><i class="fa-brands fa-discord"></i>teyllss </a>
    </article>

    <article style="display: none;">
      <hr>
      <h2>Valérian GALLE</h2>
      <p>Il n'est plus là, donc à la place il y a <a href="https://youtu.be/EZEfN5z8Mlg">ça</a>.</p>
    </article>
  </main>

  <button id="retourHaut" onclick="retourEnHaut()"><i class="fa-solid fa-circle-up"></i></button>

  <?php require("./footer.php") ?>
  <script src="script.js"></script>
</body>

</html>