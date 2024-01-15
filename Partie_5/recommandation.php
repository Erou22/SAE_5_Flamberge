<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>Recommandations</title>
    <link rel="stylesheet" type="text/css" href="style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"
        integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA=="
        crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>

<body>
<?php require("./header.php")?>

    <main>
        <form class="recommandation" action="recommandation.php" method="post">
            <div class="search-bar">
                <!-- Ajoutez ici votre code pour la barre de recherche -->
                <input type="text" placeholder="Nom du film">
                <button type="submit" class="recommandation search-button"></button>
            </div>
            <button type="button" class="recommandation methode-button" value="clusters">Méthode par clusters</button>
        </form>

    </main>

    <button id="retourHaut" onclick="retourEnHaut()"><i class="fa-solid fa-circle-up"></i></button>

    <?php require("./footer.php") ?>
</body>

</html>