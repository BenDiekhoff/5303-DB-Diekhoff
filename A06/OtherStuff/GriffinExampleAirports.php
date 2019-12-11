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

getRandomAirportPerCountry();
//print(getRandomAirportPerCountry());


//print_r(getRandomAirportPerCountry());

//print_r(findClosestWithinRadius(45.0792,23.8859,100));

//print_r(findClosestWithinRadius(45.0792,23.8859));