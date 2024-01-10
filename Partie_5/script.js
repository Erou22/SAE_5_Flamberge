// Déployer la section au clic sur le titre
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