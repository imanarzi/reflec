function myFunction(name){
    var tmstmp = Date.now();
    firebase.database().ref("/reactions").set({
        reaction: name,
        timestamp: tmstmp
      });
    console.log(name + " time: " + tmstmp);
}