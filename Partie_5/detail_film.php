<!DOCTYPE html>
<html lang="fr">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fiche film</title>
  <link rel="stylesheet" href="style.css">
  <link rel="stylesheet" href="detail_film.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"
    integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA=="
    crossorigin="anonymous" referrerpolicy="no-referrer" />
  <script src="./sidescroll.js"></script>
  <script src="loadData.js"></script>
</head>

<body>
<?php require("./header.php") ?>

  <main class="main_p_detail_film">
    <section class="section_resumer_detail">
      <article id="article_1_film_detail">
        <aside>
          <img id="affiche_film_detail" src="images/poster_sans_film.png" alt="">
        </aside>
        <div id="infos_pricipales">
          <div id="titre_note">
            <h2 id="titre_detail_film">Titre  du film qui est trop bien</h2>
            <div class="note_etoile">
            <div id="note"></div>
            </div>
          </div>
          <div id="div_button_genres">
            
          </div>
          <div id="annee">Année</div>
        </div>
      </article>
      <article id="article_2_film_detail">
        <div id="resume_detail_film">resume : ceci va être un piti resume du film, mtn il faut le rajouter à la BDD</div>
        <div id="real_detail_film">Réalisateurs</div>
      </article>
    </section>
    <section>
      <h3>Liste des acteurs et des actrices</h3>
      <div id="div_acteurs"></div>
      <h3>Liste des autres intervenants</h4>
      <div id="div_autres_intervenants"></div>
    </section>
    <script>loadFilmDetails();</script>

    <section>
      <h3>Recommendations</h3>
      <section class="film film-section" id="row-1">
        <script> loadRecommandationSimilarite(); </script>
      </section>

      <div id="bouton_reco"><button class="button" href="#">Faire plus de recommendations</button></div>
    </section>
  </main>

  <button id="retourHaut" onclick="retourEnHaut()"><i class="fa-solid fa-circle-up"></i></button>
  <?php require("./footer.php") ?>
</body>

</html>