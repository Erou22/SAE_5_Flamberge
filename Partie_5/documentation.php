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

        <section id="docu-bdd" class="clickable-section">
            <div class="section-title">
                <h2>Base de données</h2>
                <i class="fas fa-chevron-right arrow-icon"></i>
            </div>
            <div class="content" style="display: none;">
                <h4>Tables</h4>
                <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Modi illum optio voluptatum mollitia odio
                    asperiores quaerat harum nisi et accusantium natus obcaecati dolorem temporibus, suscipit id. Amet
                    aspernatur doloremque nobis.</p>
                <h4>Relations</h4>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis nobis sunt, minus, vitae itaque
                    eius, eveniet quisquam nulla repudiandae earum libero. Quo qui quasi tenetur tempora. Dolore nulla
                    quisquam ad.</p>
            </div>
        </section>

        <section id="docu-recommandation" class="clickable-section">
            <div class="section-title">
                <h2>Système de recommandation</h2>
                <i class="fas fa-chevron-right arrow-icon"></i>
            </div>
            <div class="content" style="display: none;">
                <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Modi consequatur facilis obcaecati velit,
                    nostrum aspernatur neque minima ipsam! Officiis possimus minus sunt quo maxime rerum at eius culpa,
                    reprehenderit consequuntur? Lorem, ipsum dolor sit amet consectetur adipisicing elit. Error a
                    cupiditate mollitia neque deserunt ipsum quam illum obcaecati, sequi placeat labore alias? Doloribus
                    porro, architecto error consequuntur maxime dolore assumenda? Lorem ipsum dolor sit, amet
                    consectetur adipisicing elit. Quia magnam inventore modi atque rerum, et eius placeat explicabo
                    repellat eaque repudiandae praesentium voluptate ad perspiciatis dicta ullam ipsum labore at. Lorem
                    ipsum dolor sit amet consectetur, adipisicing elit. Unde veritatis obcaecati molestias!
                    Reprehenderit ullam et blanditiis tempora laudantium obcaecati quia magni dolorum est possimus,
                    quisquam ipsa perferendis voluptatum quis aspernatur! Lorem ipsum dolor sit amet consectetur
                    adipisicing elit. Illum et dolore a perferendis ab? Molestiae veritatis velit, quaerat eveniet vitae
                    quae unde repellendus minus officia nisi doloribus, dolorum fuga exercitationem.</p>
            </div>
        </section>

        <section id="docu-api" class="clickable-section">
            <div class="section-title">
                <h2>API</h2>
                <i class="fas fa-chevron-right arrow-icon"></i>
            </div>
            <div class="content" style="display: none;">

            </div>
        </section>


        <section id="docu-installation" class="clickable-section">
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