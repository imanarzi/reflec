function myFunction(name){
    var tmstmp = Date.now();
    firebase.database().ref().set({
        reaction: name,
        timestamp: tmstmp
      });
    console.log(name + " time: " + tmstmp);
}