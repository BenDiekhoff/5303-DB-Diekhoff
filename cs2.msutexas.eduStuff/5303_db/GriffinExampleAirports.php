<?php

error_reporting(-1);

$conn = mysqli_connect('localhost', 'diekhoff', '', 'diekhoff');
if (mysqli_connect_errno()) {
    echo "Failed to connect to MySQL: " . mysqli_connect_error();
}else{
    echo "Connected...";
}


function getRandomAirportPerCountry(){
    global $conn;
    $sql = "SELECT distinct(country) FROM `a06_airports` ";
    //echo"<pre>";
    //echo"{$sql}\n";
    
    $result = $conn->query($sql);

    $airports = [];
    
    while($row = mysqli_fetch_assoc($result)){
        $sql1 = "SELECT * FROM `a06_airports` WHERE `country` = '{$row['country']}' order by RAND() LIMIT 1";
        $sub_result = $conn->query($sql1);
    
        $row2 = mysqli_fetch_assoc($sub_result);
        $airports[] = $row2;
		print_r($row2);
    }

	//return $airports;
}

function findClosestWithinRadius($lon,$lat,$distance = 0){
    global $conn;

    if($distance == 0){
        $limit = " LIMIT 1";
    }else{
        $limit = '';
    }

    echo"<pre>";

    $sql = "select *, ST_Distance_Sphere(point({$lon},{$lat}),geopoint) / 1609.3 as distance FROM a06_airports order by distance {$limit}";


    echo"$sql\n";
    $result = $conn->query($sql);

    $airports = [];

    if($distance > 0){
        while($row = mysqli_fetch_assoc($result)){
          //  print_r($row);
            if($row['distance'] < $distance){
                $airports[] = $row;
            }
        }
    }else{
        $airports =  mysqli_fetch_assoc($result);
    }

    

    return $airports;
}
getRandomAirportPerCountry();
//print(getRandomAirportPerCountry());


//print_r(getRandomAirportPerCountry());

//print_r(findClosestWithinRadius(45.0792,23.8859,100));

//print_r(findClosestWithinRadius(45.0792,23.8859));