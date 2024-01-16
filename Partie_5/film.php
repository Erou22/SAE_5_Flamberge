<?php

try {
    include('./connect.php');
    $dbh = new PDO("$driver:host=$server;dbname=$dbname", $user, $pass);
    
    $dbh -> setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $dbh -> setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
} catch (PDOException $e) {
    
    print "Erreur : " . $e->getMessage() . "<br/>";
    die();
}


function getFilmById($id){
    // la fonction qui récupère simplement un film en fonction de son id
    global $dbh;
    $sth = $dbh->prepare('SELECT * from flamberge._film where idfilm = ?');
    $sth -> execute(array($id));
    $films = $sth -> fetchAll();

    return $films[0];
}


function getNumberFilms(){
    // la fonction qui récupère simplement un film en fonction de son id
    global $dbh;
    $sth = $dbh->prepare('SELECT count (idfilm) from flamberge._film');
    $sth -> execute(array());
    $max = $sth -> fetchAll();

    return $max[0];
}


?>