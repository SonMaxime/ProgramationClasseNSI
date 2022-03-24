<!DOCTYPE html>

<html lang="fr">
    <head>
        <title>2Ways, the Comodore Game</title> <!--Titre du site-->
        <link rel="stylesheet" href="assets/css/index.css"/> <!--Importation des données CSS-->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"> <!--CSS stocké en ligne pour le bouton download-->
        <meta charset="utf-8"/>
    </head>

    <body>
        <a href="./index.html"><img src="./assets/images/Logo Jeu Two Ways.png" alt="logoDuJeu" width="10%"></a> <!--Logo du jeu-->

        <nav> <!--Création d'une navbar à plsieurs boutons-->
            <ul class="menu">
                <li>
                    <a href="./index.html">Accueil</a> <!--Redirection vers l'acceuil-->
                </li>
                <li>
                    <a href="./assets/html/navbarPages/about.html">A propos</a> <!--Redirection vers l'explication du projet-->
                </li>
                <li>
                    <a href="./assets/html/navbarPages/news.html">Nouvautés</a> <!--Redirection vers les nouvautés-->
                </li>
            </ul>
        </nav>

        <h1 align="center">2Ways ! Le jeu intéractif à choix multiple !</h1> <!--Titre du paragraphe-->

        <div class="mainConteneur">
            <p class="conteneurHome">Soyez libres de faire vos propres choix...c'est ici la thématique même de TwoWays, vous êtes le seul a pouvoir choisir et personne ne vous aidera,aucun retour en arrière ne sera possible, gare aux conséquences ! Vous pourrez choisir au début du jeu entre incarner le méchant ou le gentil de l'histoire ou même faire les deux pour une meilleure compréhension de l'histoire, mais bon comme dit plus tôt vous êtes maîtres de vos propres choix et commencer ce jeu en est un !</p>
        </div>

        <div class="menuDroite">
            <div class="menuDroiteTitre">Présentation</div>
            <ul>
                <li>
                    <a href="./assets/html/menuDroitePages/personnages.html" class="menuDroiteLink">Les personnages</a>
                </li>
            </ul>
        </div>

        <img class="traitHorizontal" src="./assets/images/traitHorizontal.png">

        <div class="downloadButton">
            <a href="./assets/download/index.zip" download="index.zip">
                <button class="btn">
                    <i class="fa fa-download"></i> Téléchager le jeu
                </button> <!--Bouton de téléchargement -->
            </a>
        </div>

        <div class="footer">Un projet Made in Sévingé</div>

        <!--Petit gif d'un chat qui viendra s'annimer quand l'utulisateur aura positionné son curseur dessus-->
        <img class="gifChat" src="./assets/images/gifNonAnimé.gif" onmouseover="this.src='assets/images/gifAnime.gif';" onmouseout="this.src='./assets/images/gifNonAnimé.gif';" />
    </body>
</html>