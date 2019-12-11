<?php

// create an array
$out = [];

// read entire file as a string csv
$csv = array_map('str_getcsv', file('airports.dat'));

$fp = fopen('a04_airports.sql','w');

foreach($csv as $row){
    
    $lat = 6;
    $lon = 7;   

    if(sizeof($row) > 14){
        $lat = 7;
        $lon = 8;
    }

    $sql = "INSERT INTO a04_airports (geoPoint) VALUES (GeomFromText('POINT({$row[$lon]} {$row[$lat]})') );\n";
    
    fwrite($fp,$sql);
}
// 