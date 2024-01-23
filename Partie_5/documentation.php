<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>Documentation</title>
    <link rel="stylesheet" type="text/css" href="style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>

<body>
    <?php require("./header.php") ?>

    <main>
        <h1>Documentation</h1>

        <section class="clickable-section">
            <div class="section-title">
                <h2>Base de données</h2>
                <i class="fas fa-chevron-right arrow-icon"></i>
            </div>
            <div class="content" style="display: none;">
                <p>Nous avons utilisé le CSV de films fournis lors de la première partie, la partie analyse de la SAÉ 5C. 
                    Ce fichier ayant assez peu de données, notre base de données est très simpliste.
                    Bien que pour cette dernière partie, il nous a fallu la modifié légèrement, car nous avons ajouter les affiches, 
                    et les descriptions de films, qui ont été récupérés grâce à du web scraping.
                </p>

                <h4>Tables</h4>
                <p>Les différentes tables sont: </p>
                <ul>
                    <li>Film : Cette table possède toutes les données concernant le film lui-même :
                        <ul>
                            <li>IdFilm</li>
                            <li>Titre</li>
                            <li>isAdult</li>
                            <li>Poster</li>
                            <li>Description</li>
                            <li>Note</li>
                            <li>NbVotes</li>
                            <li>AnnéeSortie</li>
                        </ul>
                    </li>

                    <li>Genre</li>
                    <li>Artiste</li>
                    <li>Role</li>
                    <li>Métier</li>
                </ul>


                <h4>Relations</h4>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis nobis sunt, minus, vitae itaque
                    eius, eveniet quisquam nulla repudiandae earum libero. Quo qui quasi tenetur tempora. Dolore nulla
                    quisquam ad.</p>
            </div>
        </section>

        <section class="clickable-section">
            <div class="section-title">
                <h2>Système de recommandation</h2>
                <i class="fas fa-chevron-right arrow-icon"></i>
            </div>
            <div class="content" style="display: none;">
                <p>2 idées</p>

                <h4>Par similarité item-based</h4>
                <p>

                </p>

                <h4>Grâce à des clusters</h4>
                <p>

                </p>
            </div>
        </section>

        <section class="clickable-section">
            <div class="section-title">
                <h2>API</h2>
                <i class="fas fa-chevron-right arrow-icon"></i>
            </div>
            <div class="content" style="display: none;">
                <p>Notre API </p>

                <h4>Routes</h4>
                <p>
                <strong>/</strong> : Vérifie si l'API est opérationnelle.
                <br>
                <strong>/update</strong> : Actualise les clusters et les vecteurs.
                <br>
                <strong>/recommandations/{id_film}</strong> : Retourne des recommandations de plusieurs films pour un identifiant de film donné en utilisant la méthode par défaut, les clusters. 
                <br>
                <strong>/recommandations/similarite/{id_film}</strong> : Retourne des recommandations de plusieurs films pour un identifiant de film donné en utilisant la méthode de similarité.
                <br>
                <strong>/films</strong> : Retourne la liste de tous les films.
                <br>
                <strong>/films/{id_film}</strong> : Retourne le film associé à l'identifiant donné.
                <br>
                <strong>/films/{id_film}/fiche</strong> : Retourne la fiche complète du film associé à l'identifiant donné (informations de base + acteurs + réalisateurs + autres personnes liées).
                <br>
                <strong>/films/genre/{nom_genre}</strong> : Retourne tous les films pour un genre donné (insensible à la casse).
                <br>
                <strong>/films/acteur/{id_acteur}</strong> : Retourne les films dans lesquels l'acteur donné a joué.
                <br>
                <strong>/films/realisateur/{id_realisateur}</strong> : Retourne les films réalisés par le réalisateur donné.
                <br>
                <strong>/films/autreArtiste/{id_artiste}</strong> : Retourne les films dans lesquels l'artiste donné, qui n'est ni acteur ni réalisateur, a participé.
                <br>
                <strong>/films/recherche/{titre}</strong> : Retourne des films ayant un titre proche du titre donné.
                <br>
                <strong>/genres</strong> : Retourne la liste de tous les genres.
                <br>
                <strong>/acteurs/{id_film}</strong> : Retourne la liste des acteurs pour un film donné.
                <br>
                <strong>/realisateurs/{id_film}</strong> : Retourne la liste des réalisateurs pour un film donné.
                </p>
            </div>
        </section>


        <section class="clickable-section">
            <div class="section-title">
                <h2>Installation</h2>
                <i class="fas fa-chevron-right arrow-icon"></i>
            </div>
            <div class="content" style="display: none;">

            </div>
        </section>
    </main>

    <button id="retourHaut" onclick="retourEnHaut()"><i class="fa-solid fa-circle-up"></i></button>

    <?php require("./footer.php") ?>
</body>

</html>