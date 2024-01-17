<!DOCTYPE html>
<html lang="fr">

<head>
  <?php require("./film.php") ?>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Recherche</title>
  <link rel="stylesheet" href="style.css">
  <link rel="stylesheet" href="carousel.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
  <script> let resultat= "<?php echo $_GET["search"]?>";</script>
  <script src="./loadData.js"></script>
  <script>loadRecherche();</script>
</head>

<body>
  <?php require("./header.php") ?>
  <main>
    <section class="result">
        <h3> Résultats de recherche pour <?php echo $_GET["search"] ?>  </h3>

        <div class="ligneResult">
            <img src="./images/logo_loupe.png" alt="titre"/>
            <div class="desc">
              <h4>Le titre du film</h4>
              <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Modi illum optio voluptatum mollitia odio
                asperiores quaerat harum nisi et accusantium natus obcaecati dolorem temporibus, suscipit id. Amet
                aspernatur doloremque nobis.</p>
                <aside>
                <div>★</div>
                <div>6.4</div>
              </aside>
              <div class="real"> Réalisateur: <a> Jean </a></div>
            </div>
        </div>
    </section>
  </main>

  <button id="retourHaut" onclick="retourEnHaut()"><i class="fa-solid fa-circle-up"></i></button>

  <?php require("./footer.php") ?>
</body>
</html>