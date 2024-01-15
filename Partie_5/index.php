<!DOCTYPE html>
<html lang="fr">

<head>
  <?php require("./film.php") ?>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ma Page d'Accueil</title>
  <link rel="stylesheet" href="style.css">
  <link rel="stylesheet" href="carousel.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>

<body>
  <?php require("./header.php") ?>
  <main>

    <section class="laUne">
      <div class="carousel">

        <input type="radio" id="carousel-css-slide-1" name="carousel-css" value="slide-1" checked />
        <input type="radio" id="carousel-css-slide-2" name="carousel-css" value="slide-2" />
        <input type="radio" id="carousel-css-slide-3" name="carousel-css" value="slide-3" />
        <input type="radio" id="carousel-css-slide-4" name="carousel-css" value="slide-4" />

        <label for="carousel-css-slide-1" data-value="slide-1"></label>
        <label for="carousel-css-slide-2" data-value="slide-2"></label>
        <label for="carousel-css-slide-3" data-value="slide-3"></label>
        <label for="carousel-css-slide-4" data-value="slide-4"></label>

        <div class="carousel-wrapper">
          <div class="carousel-slide">
            <div class="img"><img src="./images/flamberge.png"></div>
            <div class="description">
              <h4>Le titre du film</h4>
              <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Modi illum optio voluptatum mollitia odio
                asperiores quaerat harum nisi et accusantium natus obcaecati dolorem temporibus, suscipit id. Amet
                aspernatur doloremque nobis.</p>
              <aside>
                <div>★</div>
                <div>6.4</div>
              </aside>
            </div>
          </div>
          <div class="carousel-slide">
            <div class="img"><img src="./images/logo_loupe.png"></div>
            <div class="description"></div>
          </div>
          <div class="carousel-slide">
            <div class=".img"></div>
            <div class="description"></div>
          </div>
          <div class="carousel-slide">
            <div class=".img"></div>
            <div class="description"></div>
          </div>
        </div>
      </div>
    </section>


    <section class="film">
      <article>
        <img src="./images/logo_loupe.png">
        <h3 class="">Titre du film</h3>
        <aside>
          <div>★</div>
          <div>6.4</div>
        </aside>
      </article>

      <article>
        <img src="./images/logo_loupe.png">
        <h3 class="">Titre du film</h3>
        <aside>
          <div>★</div>
          <div>6.4</div>
        </aside>
      </article>

      <article>
        <img src="./images/logo_loupe.png">
        <h3 class="">Titre du film</h3>
        <aside>
          <div>★</div>
          <div>6.4</div>
        </aside>
      </article>

      <article>
        <img src="./images/logo_loupe.png">
        <h3 class="">Titre du film</h3>
        <aside>
          <div>★</div>
          <div>6.4</div>
        </aside>
      </article>

      <article>
        <img src="./images/logo_loupe.png">
        <h3 class="">Titre du film</h3>
        <aside>
          <div>★</div>
          <div>6.4</div>
        </aside>
      </article>

      <article>
        <img src="./images/logo_loupe.png">
        <h3 class="">Titre du film</h3>
        <aside>
          <div>★</div>
          <div>6.4</div>
        </aside>
      </article>

      <article>
        <img src="./images/logo_loupe.png">
        <h3 class="">Titre du film</h3>
        <aside>
          <div>★</div>
          <div>6.4</div>
        </aside>
      </article>

      <article>
        <img src="./images/logo_loupe.png">
        <h3 class="">Titre du film</h3>
        <aside>
          <div>★</div>
          <div>6.4</div>
        </aside>
      </article>

      <article>
        <img src="./images/logo_loupe.png">
        <h3 class="">Titre du film</h3>
        <aside>
          <div>★</div>
          <div>6.4</div>
        </aside>
      </article>

      <article>
        <img src="./images/logo_loupe.png">
        <h3 class="">Titre du film</h3>
        <aside>
          <div>★</div>
          <div>6.4</div>
        </aside>
      </article>

      <article>
        <img src="./images/logo_loupe.png">
        <h3 class="">Titre du film</h3>
        <aside>
          <div>★</div>
          <div>6.4</div>
        </aside>
      </article>

    </section>
  </main>

  <button id="retourHaut" onclick="retourEnHaut()"><i class="fa-solid fa-circle-up"></i></button>

  <?php require("./footer.php") ?>
</body>


</html>