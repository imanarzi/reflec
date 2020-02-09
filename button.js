function myFunction(name){

    var user = "izzi";
    var tmstmp = Date.now();
    /*var newDBRef = firebase.database().ref("/test").push();
    newDBRef.update({
        reaction: name,
        timestamp: tmstmp
      }); */
      var params = JSON.stringify({ "reaction": name});
      var xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
          //alert("no!");
        }
      };
      xhttp.open('PUT', "https://reflec-46d2b.firebaseio.com/" + user + "/" + tmstmp + ".json", true);
      xhttp.setRequestHeader('Content-type', 'application/json');
      //console.log("hi");
      console.log(params);

      xhttp.send([params]);
      
      // curl -X PUT -d '{
      //   "alanisawesome": {
      //     "name": "Alan Turing",
      //     "birthday": "June 23, 1912"
      //   }
      // }' 'https://reflec-46d2b.firebaseio.com/reacts.json'
      


}