
function getFilmIdFromUrl() {
  // Récupère la chaîne de requête de l'URL
  var queryString = window.location.search;

  // Crée un objet URLSearchParams avec la chaîne de requête
  var urlSearchParams = new URLSearchParams(queryString);

  // Obtient la valeur de 'idFilm' de la chaîne de requête
  var idFilm = urlSearchParams.get('idFilm');

  return idFilm;
}

function getGenreFromUrl() {
  // Récupère la chaîne de requête de l'URL
  var queryString = window.location.search;

  // Crée un objet URLSearchParams avec la chaîne de requête
  var urlSearchParams = new URLSearchParams(queryString);

  // Obtient la valeur de 'genre' de la chaîne de requête
  var genre = urlSearchParams.get('genre');

  return genre;
}

function getIdArtisteFromUrl() {
  // Récupère la chaîne de requête de l'URL
  var queryString = window.location.search;

  // Crée un objet URLSearchParams avec la chaîne de requête
  var urlSearchParams = new URLSearchParams(queryString);

  // Obtient la valeur de 'idArtiste' de la chaîne de requête
  var idArtiste = urlSearchParams.get('idArtiste');

  return idArtiste;
}

function getArtistTypeFromURL() {
  // Récupère la chaîne de requête de l'URL
  var queryString = window.location.search;

  // Crée un objet URLSearchParams avec la chaîne de requête
  var urlSearchParams = new URLSearchParams(queryString);

  // Obtient la valeur de 'type' de la chaîne de requête
  var type = urlSearchParams.get('type');

  return type;
}

function loadRecherche() {
  // Assuming `resultat` is the variable holding the "titre" value
  let resultatModified = resultat.replace(/ /g, '+');

  let xhr = new XMLHttpRequest();
  xhr.open('GET', 'http://127.0.0.1:8000/films/recherche/' + resultatModified, true);
  xhr.onload = function () {
    if (this.status == 200) {
      let obj = JSON.parse(this.responseText);
      //console.log(obj.films);

      if (obj.films.length > 0) {
        obj.films.forEach(film => {
          addData(film);
        });
      } else {
        displayNoResultsMessage("Aucun film n'a été trouvé avec le titre " + resultat);
      }
    } else if (this.status == 404) {
      let obj = JSON.parse(this.responseText);
      //console.log(obj.error);
      displayNoResultsMessage(obj.error);
    }
  }
  xhr.send();
}

function displayNoResultsMessage(message) {
  // Create a new element for the message
  var noResultsElement = document.createElement("div");
  noResultsElement.textContent = message;
  noResultsElement.classList.add("no-results-message"); // You can add a class for styling if needed

  // Append the message element to the result container
  var resultContainer = document.getElementById("result");
  resultContainer.appendChild(noResultsElement);
}

function addData(film) {
  var res = document.getElementById("result");

  // Creating the container for each film result
  var ligne = document.createElement("div");
  ligne.classList.add("ligneResult");

  // Creating the film details link
  var filmLink = document.createElement("a");
  filmLink.href = "http://localhost:8080/detail_film.php?idFilm=" + film.idFilm;

  // Creating the film poster image
  var img = document.createElement("img");

  console.log(film.poster)
  if (film.poster != "\\N") {
    img.src = film.poster;
  } else {
    img.src = './images/poster_sans_film.png'
  }



  img.alt = film.titre;

  // Creating the description container
  var desc = document.createElement("div");
  desc.classList.add("desc");

  // Creating the film title
  var titre = document.createElement("h4");
  titre.innerHTML = film.titre;

  
  // Creating the film description
  var description = document.createElement("p");
  var originalText = film.description


  if (originalText.length > 400) {
    description.innerHTML = originalText.substring(0, 400) + "...";
  } else {
    if(originalText!='\\N'){
      description.innerHTML = originalText;
    }else{
      description.innerHTML = 'Aucune description pour ce film.'
    }
  }

  // Creating the aside container for rating and note
  var aside = document.createElement("aside");
  
  
  var etoile = document.createElement("div");
  etoile.innerHTML = "★";
  var note = document.createElement("div");
  note.innerHTML = film.note;


  // Creating the container for the director information
  var real = document.createElement("div");

  // Fetching director information using XMLHttpRequest
  let xhr = new XMLHttpRequest();
  xhr.open("GET", "http://127.0.0.1:8000/realisateurs/" + film["idFilm"], true);
  listreal = [];
  xhr.onload = function () {
    if (this.status == 200) {
      let realisateurs = JSON.parse(this.responseText).director;
      if (realisateurs && realisateurs.length > 0) {
        for (let i = 0; i < realisateurs.length; i++) {
          listreal.push(realisateurs[i].nomArtiste);
        }
        if (listreal.length > 1) {
          real.innerHTML = "Réalisateurs : " + listreal.join(", ");
        } else {
          real.innerHTML = "Réalisateur : " + listreal[0];
        }
      } else {
        real.innerHTML = "Réalisateur : inconnu";
      }
    } else if (this.status == 404) {
      real.innerHTML = "Réalisateur : inconnu";
    }
  };
  xhr.send();

  // Creating the "Faire plus de recommendations" button
  var recoButton = document.createElement("button");
  recoButton.classList.add("button");
  recoButton.innerHTML = "Faire plus de recommendations";

  recoButton.addEventListener("click", function (event) {
    // Prevent the link's default behavior when the button is clicked
    event.preventDefault();
    // Redirect to the recommendation page
    window.location.href = "recommandation.php?idFilm=" + film.idFilm;
  });

  // Appending elements to the document
  res.appendChild(filmLink);
  filmLink.appendChild(ligne);
  ligne.appendChild(img);
  ligne.appendChild(desc);
  desc.appendChild(titre);
  desc.appendChild(description);
  desc.appendChild(aside);
  real.classList.add("real");
  desc.appendChild(real);
  recoButton.style.marginTop = "2em"; // Adjusting the button margin
  desc.appendChild(recoButton); // Adding the button to the desc element
  if(film.note!=-1){
  aside.appendChild(etoile);
  aside.appendChild(note);
  }
}








// Permet de remplir la page de détails d'un film
function loadFilmDetails() {
  // Récupère l'id du film dans la page, et l'envoie à l'API
  let id = getFilmIdFromUrl();
  //console.log(id)
  let div_genres = document.getElementById("div_button_genres");
  let xhr = new XMLHttpRequest();
  xhr.open('GET', 'http://127.0.0.1:8000/films/' + id + '/fiche', true);
  xhr.onload = function () {
    if (this.status == 200) {
      let film = JSON.parse(this.responseText).film[0];
      document.getElementById("titre_detail_film").innerHTML = film.titre;
      document.querySelector("title").innerHTML = film.titre + " - Fiche film";
      document.getElementById('reco_link').setAttribute('href', 'recommandation.php?idFilm=' + getFilmIdFromUrl());

      if (film.poster != '\\N') {
        document.getElementById("affiche_film_detail").src = film.poster
      } else {
        document.getElementById("affiche_film_detail").src = './images/poster_sans_film.png'
      }

      if (film.description != '\\N') {
        document.getElementById("resume_detail_film").innerHTML = film.description;
      } else {
        document.getElementById("resume_detail_film").innerHTML = "Aucune description pour ce film."
        document.getElementById("resume_detail_film").style.color = "lightgrey";
      }

      document.getElementById("annee").innerHTML = film.annee;

      if (film.note != -1) {
        document.getElementById("note").innerHTML = film.note + '★';
      }


      for (let i = 0; i < film.genres.length; i++) {
        let genre = film.genres[i];
        let button = document.createElement("button");
        button.innerHTML = genre;
        button.onclick = function () {
          window.location.href = "http://localhost:8080/genre.php?genre=" + genre;
        }
        div_genres.appendChild(button);
      }
      let acteurs = film.artistes.Acteurs;
      let realisateurs = film.artistes.Réalisateur;
      let autres = film.artistes.Autres;
      let div_realisateurs = document.getElementById("real_detail_film");
      let div_acteurs = document.getElementById("div_acteurs");
      let div_autres = document.getElementById("div_autres_intervenants");
      // Création des boutons pour les acteurs
      if (typeof acteurs !== "string") {
        for (let i = 0; i < acteurs.length; i++) {
          let acteur = acteurs[i];
          let button = document.createElement("button");
          button.classList.add("people");
          button.innerHTML = acteur.nomArtiste;
          button.onclick = function () {
            window.location.href = "http://localhost:8080/artiste.php?type=acteur&idArtiste=" + acteur.idArtiste;
          }
          div_acteurs.appendChild(button);
        }
      } else {
        div_acteurs.innerHTML = "Aucun acteur/actrice n'est répertorié pour ce film.";
        div_acteurs.style.color = "lightgrey";
      }
      // Création des boutons pour les réalisateurs
      if (typeof realisateurs !== "string") {
        if (realisateurs.length > 1) {
          div_realisateurs.innerHTML = "Réalisateurs : ";
        } else {
          div_realisateurs.innerHTML = "Réalisateur : ";
        }
        for (let i = 0; i < realisateurs.length; i++) {
          let realisateur = realisateurs[i];
          let button = document.createElement("button");
          button.classList.add("people");
          button.innerHTML = realisateur.nomArtiste;
          button.onclick = function () {
            window.location.href = "http://localhost:8080/artiste.php?type=realisateur&idArtiste=" + realisateur.idArtiste;
          }
          div_realisateurs.appendChild(button);
        }
      } else {
        div_realisateurs.innerHTML = "Aucun réalisateur n'est répertorié pour ce film.";
        div_realisateurs.style.color = "lightgrey";
      }
      // Création des roles et des boutons pour les autres intervenants
      if (typeof autres !== "string") {
        let liste_roles = []
        for (let i = 0; i < autres.length; i++) {
          let autre = autres[i];
          if (!liste_roles.includes(autre.nomRole)) {
            liste_roles.push(autre.nomRole);
            let div_role = document.createElement("div");
            div_role.innerHTML = autre.nomRole + " : ";
            div_role.id = autre.nomRole;
            div_role.style.marginBottom = "0.25em";
            div_autres.appendChild(div_role);
          }
          let button = document.createElement("button");
          let div_role = document.getElementById(autre.nomRole);
          button.classList.add("people");
          button.innerHTML = autre.nomArtiste;
          button.onclick = function () {
            window.location.href = "http://localhost:8080/artiste.php?type=autre+artiste&idArtiste=" + autre.idArtiste;
          }
          div_role.appendChild(button);
        }
      } else {
        div_autres.innerHTML = "Aucun autre intervenant(e) n'est répertorié(e) pour ce film.";
        div_autres.style.color = "lightgrey";
      }
    }
  }
  xhr.send();
}



function loadGenre() {
  let genre = getGenreFromUrl();
  let h3_genres = document.querySelector(".result > h3");
  h3_genres.innerHTML += genre + "\"";
  document.querySelector("title").innerHTML = genre + " - Films";

  let xhr = new XMLHttpRequest();
  xhr.open('GET', 'http://127.0.0.1:8000/films/genre/' + genre, true);
  xhr.onload = function () {
    if (this.status == 200) {
      let films = JSON.parse(this.responseText).films;
      //console.log(films);

      if (films.length > 0) {
        films.slice(0, 10).forEach(film => {
          addData(film);
        });
      } else {
        displayNoResultsMessage("Aucun film n'a été trouvé avec le genre " + genre);
      }
    } else if (this.status == 404) {
      let obj = JSON.parse(this.responseText);
      //console.log(obj.error);
      displayNoResultsMessage(obj.error);
    }
  }
  xhr.send();
}


function addGenre(genre) {
  let div_genres = document.getElementById("div_genres");
  let anchor = document.createElement("a");
  anchor.innerHTML = genre;
  anchor.onclick = function () {
    window.location.href = "http://localhost:8080/genre.php?genre=" + genre;
  }
  div_genres.appendChild(anchor);
}


function loadGenres() {
  let xhr = new XMLHttpRequest();
  xhr.open('GET', 'http://127.0.0.1:8000/genres', true);
  xhr.onload = function () {
    if (this.status == 200) {
      let genres = JSON.parse(this.responseText).genres.sort();
      //console.log(genres);

      if (genres.length > 0) {
        genres.forEach(genre => {
          addGenre(genre);
        });
      }
    }
  }
  xhr.send();
}


function loadArtiste() {
  let id = getIdArtisteFromUrl();
  let type = getArtistTypeFromURL();
  let xhr = new XMLHttpRequest();
  txt=document.querySelector(".result > h3");
  if (type == "acteur") {
    xhr.open('GET', 'http://127.0.0.1:8000/films/acteur/' + id, true);
    txt.innerHTML = "Filmographie de l'acteur.ice : "
  } else if (type == "realisateur") {
    xhr.open('GET', 'http://127.0.0.1:8000/films/realisateur/' + id, true);
    txt.innerHTML = "Filmographie du réalisateur.ice : "
  } else {
    xhr.open('GET', 'http://127.0.0.1:8000/films/autreArtiste/' + id, true);
    txt.innerHTML = "Filmographie de l'intervenant : "
  }
  xhr.onload = function () {
    if (this.status == 200) {
      let films = JSON.parse(this.responseText).films;
      //console.log(films);

      if (films.length > 0) {
        films.slice(0, 10).forEach(film => {
          addData(film);
        });
      } else {
        displayNoResultsMessage("Aucun film n'a été trouvé avec cet artiste.");
      }
    } else if (this.status == 404) {
      let obj = JSON.parse(this.responseText);
      //console.log(obj.error);
      displayNoResultsMessage(obj.error);
    }
  }
  xhr.send();
}