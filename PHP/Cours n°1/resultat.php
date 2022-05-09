<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Utilisation de PHP</title>
    </head>
    <body>
        <?php
        if (isset($_POST["PrixDuM²"])) {
            $prix2 = $_POST["PrixDuM²"];
            echo "Prix du m²: $prix2\n";
        } else {
            echo "La valeur n'existe pas.";
        }
        if (isset($_POST["LongueurDuTerrain"])) {
            $long = $_POST["LongueurDuTerrain"];
            echo "Longueur du terrain: $long\n";
        } else {
            echo "La valeur n'existe pas.";
        }
        if (isset($_POST["LargeurDuTerrain"])) {
            $larg = $_POST["LargeurDuTerrain"];
            echo "Largeur du terrain: $larg\n";
        } else {
            echo "La valeur n'existe pas";
        }

        if (isset($_POST["PrixDuM²"], $_POST["LongueurDuTerrain"], $_POST["LargeurDuTerrain"])) {
            $prix = $_POST['PrixDuM²'] * $_POST['LongueurDuTerrain'] * $_POST['LargeurDuTerrain'];
            echo "Le prix de votre terrain est de: $prix";
        } else {
            echo "Des informations n'ont pas été provenues, je ne peux donc pas effectuer le calcul.";
        }
        ?>
    </body>
</html>