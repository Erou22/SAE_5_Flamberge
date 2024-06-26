<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>Genre</title>
    <link rel="stylesheet" type="text/css" href="style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <script src="loadData.js"></script>
</head>

<body>
    <?php require("./header.php") ?>

    <main>
        <section class="result" id="result">
            <h3>Films du genre "</h3>
        </section>
    </main>

    <button id="retourHaut" onclick="retourEnHaut()"><i class="fa-solid fa-circle-up"></i></button>

    <?php require("./footer.php") ?>
    <script>
        loadGenre();
    </script>
</body>

</html>