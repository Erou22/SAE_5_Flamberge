// Afficher le menu burger
function toggleMenu() {
    var nav = document.querySelector('nav');
    nav.classList.toggle('show');
}

/* ----------------------- */
/*  Bouton retour en haut  */
/* ----------------------- */

window.onscroll = function () {
    afficherBouton();
};

function afficherBouton() {
    var boutonRetourHaut = document.getElementById("retourHaut");
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        boutonRetourHaut.style.display = "block";
    } else {
        boutonRetourHaut.style.display = "none";
    }
}

// Fonction pour retourner en haut de la page
function retourEnHaut() {
    document.body.scrollTop = 0; // Pour les navigateurs Safari
    document.documentElement.scrollTop = 0; // Pour les autres navigateurs
}

/* -------------------------------- */
/*  Documentation - Menu déroulant  */
/* -------------------------------- */
document.addEventListener("DOMContentLoaded", function () {
    const clickableSections = document.querySelectorAll(".clickable-section");

    clickableSections.forEach(function (section) {
        section.addEventListener("click", function (event) {
            const content = this.querySelector(".content");
            const arrowIcon = this.querySelector(".arrow-icon");

            if (content.contains(event.target)) {
                return; // Clic à l'intérieur du contenu, pas de changement
            }

            content.style.display = (content.style.display === "none") ? "block" : "none";

            // Met à jour l'orientation de la flèche
            if (content.style.display === "none") {
                arrowIcon.classList.remove("fa-chevron-down");
                arrowIcon.classList.add("fa-chevron-right");
            } else {
                arrowIcon.classList.remove("fa-chevron-right");
                arrowIcon.classList.add("fa-chevron-down");
            }
        });
    });
});