
function loadRecherche(){
let xhr = new XMLHttpRequest();
xhr.open('GET', 'http://127.0.0.1:8000/films/recherche/'+resultat, true);
xhr.onload = function () {
  if (this.status == 200) {
    let obj = JSON.parse(this.responseText);
    console.log(obj.films)
    obj.films.forEach(film => {
        addData(film)
    });
    }
}
xhr.send();
}

function addData(film){
    var res=document.getElementById("result")
    var ligne=document.createElement("div")
    ligne.classList.add("ligneResult")
    var img=document.createElement("img")
    img.src="./images/logo_loupe.png"
    img.alt=film["titre"]
    var desc=document.createElement("div")
    desc.classList.add("desc")
    var titre=document.createElement("h4")
    titre.innerHTML=film["titre"]
    var description=document.createElement("p")
    description.innerHTML="Lorem ipsum"
    var aside=document.createElement("aside")
    var etoile=document.createElement("div")
    etoile.innerHTML = "★"
    var note=document.createElement("div")
    note.innerHTML=film["note"]
    var real=document.createElement("div")
    real.classList.add("real")
    real.innerHTML= "Réalisateur : réal"

    res.appendChild(ligne)
    ligne.appendChild(img)
    ligne.appendChild(desc)
    desc.appendChild(titre)
    desc.appendChild(description)
    desc.appendChild(aside)
    desc.appendChild(real)
    aside.appendChild(etoile)
    aside.appendChild(note)
    

}