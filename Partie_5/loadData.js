
function loadRecherche(){
let xhr = new XMLHttpRequest();
xhr.open('GET', 'http://127.0.0.1:8000/films/recherche/'+resultat, true);
xhr.onload = function () {
  if (this.status == 200) {
    let obj = JSON.parse(this.responseText);
    console.log(obj.films)
    obj.films.forEach(film => {
        console.log(film["titre"])
    });
    }
}
xhr.send();
}