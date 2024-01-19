<!DOCTYPE html>
<html lang="fr">

<head>
  <?php //require("./film.php") ?>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fiche film</title>
  <link rel="stylesheet" href="style.css">
  <link rel="stylesheet" href="detail_film.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"
    integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA=="
    crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>

<body>
<?php require("./header.php") ?>

  <main class="main_p_detail_film">
    <section class="section_resumer_detail">
      <article id="article_1_film_detail">
        <aside>
          <img id="affiche_film_detail" src="images/logo_loupe.png" alt="">
        </aside>
        <div id="infos_pricipales">
          <div id="titre_note">
            <h2 id="titre_detail_film">Titre  du film qui est trop bien</h2>
            <div class="note_etoile">
              <div id="note">6.4</div>
              <div>★</div>
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
    <script src=loadData.js></script>
    <script>loadFilmDetails();</script>
    <section>
      <h3>Recommendations</h3>
      <div class="film_reco">
        <section class="film">
          <article class="detail_film_recommendation">
            <img src="./images/logo_loupe.png">
            <h3 class="">Titre du film</h3>
            <aside>
              <div>★</div>
              <div>6.4</div>
            </aside>
          </article>
    
          <article class="detail_film_recommendation">
            <img src="./images/logo_loupe.png">
            <h3 class="">Titre du film</h3>
            <aside>
              <div>★</div>
              <div>6.4</div>
            </aside>
          </article>
    
          <article class="detail_film_recommendation">
            <img src="./images/logo_loupe.png">
            <h3 class="">Titre du film</h3>
            <aside>
              <div>★</div>
              <div>6.4</div>
            </aside>
          </article>

          <article class="detail_film_recommendation">
            <img src="./images/logo_loupe.png">
            <h3 class="">Titre du film</h3>
            <aside>
              <div>★</div>
              <div>6.4</div>
            </aside>
          </article>

          <article class="detail_film_recommendation">
            <img src="./images/logo_loupe.png">
            <h3 class="">Titre du film</h3>
            <aside>
              <div>★</div>
              <div>6.4</div>
            </aside>
          </article>

          <article class="detail_film_recommendation">
            <img src="./images/logo_loupe.png">
            <h3 class="">Titre du film</h3>
            <aside>
              <div>★</div>
              <div>6.4 <span class="weak">(1500)<span></div>
            </aside>
          </article>
      </div>
      <div id="bouton_reco"><a href="#" id="reco_link"><button class="button">Faire plus de recommendations</button></a></div>
    </section>
  </main>

  <button id="retourHaut" onclick="retourEnHaut()"><i class="fa-solid fa-circle-up"></i></button>

  <?php require("./footer.php") ?>
</body>

</html>