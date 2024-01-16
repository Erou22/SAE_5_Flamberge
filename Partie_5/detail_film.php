<!DOCTYPE html>
<html lang="fr">

<head>
  <?php require("./film.php") ?>
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
            <h2>Titre  du film qui est trop bien</h2>
            <div class="note_etoile">
              <div>6.4</div>
              <div>★</div>
            </div>
          </div>
          <div>
            <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"><button>Genre 1</button></a>
            <a href="https://www.youtube.com/watch?v=OVh0bMNSFss"><button>Genre 2</button></a>
            <a href="https://www.youtube.com/watch?v=EUc1AhTdG3U"><button>Genre 3</button></a>
          </div>
          <div>Année</div>
        </div>
      </article>
      <article id="article_2_film_detail">
        <div>resume : ceci va être un piti resume du film, mtn il faut le rajouter à la BDD</div>
        <div>Realisateurs</div>
        <div>2-3 acteurs</div>
      </article>
    </section>
    <section>
      <h3>Liste des acteurs</h3>
      <div>La liste des acteurs</div>
      <h4>Liste des autres intervenants</h4>
    </section>
    <section>
      <h3>Reco</h3>
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
      <div id="bouton_reco"><a href="recommandation.php"><button class="button">Faire des recommendations</button></a></div>
    </section>
  </main>

  <button id="retourHaut" onclick="retourEnHaut()"><i class="fa-solid fa-circle-up"></i></button>

  <?php require("./footer.php") ?>
</body>

</html>