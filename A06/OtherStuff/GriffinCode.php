<?php

error_reporting(-1);

// connect to db
$conn = mysqli_connect('localhost', '5303', '', '5303');
if (mysqli_connect_errno()) {
    echo "Failed to connect to MySQL: " . mysqli_connect_error();
}else{
    echo "Connected...";
}


/**
 * getRandomAirportPerCountry
 * 
 * 
 */
function getRandomAirportPerCountry(){

    // global keyword allows access to variable declared outside of code block
    global $conn;

    // Create the sql statement
    $sql = "SELECT distinct(country) FROM `airports` ";

    // preformat tag = respect newlines and whitespace
    // otherwise all text will be crammed together
    echo"<pre>";

    // print the statement
    echo"{$sql}\n";
    
    // run query
    $result = $conn->query($sql);

    // create an empty array
    $airports = [];
    
    // while there are more rows in the query result
    while($row = mysqli_fetch_assoc($result)){
        
        // create a sub query
        $sql1 = "SELECT * FROM `airports` WHERE `country` = '{$row['country']}' order by RAND() LIMIT 1";

        // run sub query
        $sub_result = $conn->query($sql1);
        
        // get single row result of sub query
        $row2 = mysqli_fetch_assoc($sub_result);
        
        // push that result onto our array
        $airports[] = $row2;
    
    }

    // return resulting array
    return $airports;
}

/**
 * findClosestWithinRadius
 * 
 * Params:
 *      $lon        : x coord
 *      $lat        : y coord
 *      $distance   : radius 
 */
function findClosestWithinRadius($lon,$lat,$distance = 0){
    global $conn;   // same as previous comment

    // if default param then only return a single value
    if($distance == 0){
        $limit = " LIMIT 1";
    }else{
        // otherwise don't use a limit on the query
        $limit = '';
    }

    // respect whitespace and newlines
    echo"<pre>";

    // select everything, and the distance from `geopoint` to (lon,lat)
    // if $limit is set to one, the result will have the closest airport
    $sql = "select *, ST_Distance_Sphere(point({$lon},{$lat}),geopoint) / 1609.3 as distance FROM airports order by distance {$limit}";


    // print the query
    echo"$sql\n";

    // run the query
    $result = $conn->query($sql);

    //create an empty array
    $airports = [];

    // if distance > 0 we want more than a single match
    if($distance > 0){
        while($row = mysqli_fetch_assoc($result)){
          //  print_r($row);
            if($row['distance'] < $distance){
                $airports[] = $row;
            }
        }
    }else{
        // give us a single closest result
        $airports =  mysqli_fetch_assoc($result);
    }

    
    // return result
    return $airports;
}


//////////////////////////////////////////////////
// USED AS HELP TO BUILD ASSOC ARRAY CORRECTLY TO REPRESENT GEOJSON
// {
//     "type=>FeatureCollection",
//     "features": [
//       {
//         "type=>Feature",
//         "geometry": {
//           "type=>Point",
//           "coordinates": [
//             -103.71093749999999,
//             41.244772343082076
//           ]
//         },
//         "properties": {
//           "title=>Starting Point",
//           "description=>Somewhere in the US",
//           "marker-size=>medium",
//           "marker-symbol=>airport",
//           "marker-color=>#f00",
//           "stroke=>#555555",
//           "stroke-opacity": 1,
//           "stroke-width": 2,
//           "fill=>#555555",
//           "fill-opacity": 0.5
//         }
//       }

// [236] => Array
// (
//     [airport_id] => 7674
//     [name] => Wake Island Airfield
//     [city] => Wake island
//     [country] => Wake Island
//     [longitude] => 166.63600158691406
//     [latitude] => 19.282100677490234
//     [geopoint] =>  Z�d@�7H3@
// )
///////////////////////////////

/**
 * getGeoJson
 * 
 * Description:
 *      Selects data from Diekhoff's DB and formats the results to be valid geojson
 */
function getGeoJson(){
    $json = [];                         // empty json array
    $json['type']='FeatureCollection';  // add top level key to be a 'FeatureCollection'
    $json['features'] = [];            // now push on an array with the key 'features'

    // get a bunch of airports
    $airports = getRandomAirportPerCountry();

    // loop through result set and build a php associative array to be encoded as a json (geojson) object
    foreach($airports as $airport){
        // push a new "object" (feature) onto our features array
        $json['features'][] = ['type'=>'Feature',
                                'geometry'=>[
                                    'type'=>'Point',
                                    'coordinates'=>[$airport['longitude']*1.0,$airport['latitude']*1.0]],
                                    "properties"=> [
                                        "title" =>"Starting Point",
                                        "description"=>"Somewhere in the US",
                                        "marker-size"=>"medium",
                                        "marker-symbol"=>"airport",
                                        "marker-color"=>"#f00",
                                        "stroke"=>"#555555",
                                        "stroke-opacity" =>1,
                                        "stroke-width"=>2,
                                        "fill" => "#555555",
                                        "fill-opacity" => 0.5
                                    ]
                                ]; 
    }
    
    // dump to output (json pretty adds newlines and indentation)
    print_r(json_encode($json,JSON_PRETTY_PRINT));

}

/**
 * updateDistance
 * Description:
 *      Update the cities and airports table to have the distance between the city and airport
 */
function updateDistance(){
    global $conn;
    $sql = "SELECT *,ST_Distance(`airport_geopoint`,`city_geopoint`) as distance FROM `citiesAndAirports`";
    $result = $conn->query($sql);

    $airports = [];
    
    // make unique
    while($row = mysqli_fetch_assoc($result)){
        $airports[$row['airport_name']] = $row;
    }


    print_r($airports);

    $i = 0;
    // added $key => $airport (so we grab the )
    // each iteration $key will be the airport name 
    // but since its also in the $airport array we can
    // ignore it ($key).
    foreach($airports as $key => $airport){
        $a = $airport['airport_name'];
        $b = $airport['city_name'];
        $c = $airport['airport_geopoint'];
        $d = $airport['city_geopoint'];
        $e = $airport['distance'];

        $sql = "INSERT INTO citiesAndAirports2 VALUES ('{$i}','{$a}','{$b}','{$c}','{$d}','{$e}')";

        $res = $conn->query($sql);

        if(!$res){
            printf("Errormessage: %s\n", $conn->error);
        }
        print_r($sql);
        $i++;
    }
}



print_r(getRandomAirportPerCountry());

//getGeoJson();


//updateDistance();

//print_r(findClosestWithinRadius(45.0792,23.8859,100));

//print_r(findClosestWithinRadius(45.0792,23.8859));
