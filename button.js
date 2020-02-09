function myFunction(name){
  var user = "izzi";
  var tmstmp = Date.now();
  var params = JSON.stringify({ "reaction": name});
  var xhttp = new XMLHttpRequest();
    xhttp.open('PUT', "https://reflec-46d2b.firebaseio.com/" + user + "/" + tmstmp + ".json", true);
    xhttp.setRequestHeader('Content-type', 'application/json');
    console.log(params);
    xhttp.send([params]);
}