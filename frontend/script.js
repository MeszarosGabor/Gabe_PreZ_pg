/*
 * Main frontend interaction implementation including API calls.
 */

document.getElementById("getTitleData").addEventListener("click", getTitleData);
document.getElementById("getAllData").addEventListener("click", getAllData);

// Fetch all data for a given title.
function getTitleData() {
    var xhttp = new XMLHttpRequest();
    var title = document.getElementById("titleField").value;
    var url = "http://127.0.0.1:18871/search/?title=" + title;
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
           var myArr = JSON.parse(this.responseText);
           var out = "";
           var i;
           for(i = 0; i < myArr.length; i++) {
               out += '<p>' + JSON.stringify(myArr[i]); + '</p>'
           }
           document.getElementById("msg").innerHTML = out;
        }
    };
    xhttp.open("GET", url, true);
    xhttp.send();
};

// Fetch all data.
function getAllData() {
    var xhttp = new XMLHttpRequest();
    // TODO: fix the is_sorted checkbox!!!
    var is_sorted = Boolean(document.getElementById("sorted").value);
    console.log("Is sorted: ", is_sorted);
    var url = "http://127.0.0.1:18871/search/?sorted="+is_sorted;
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
           var myArr = JSON.parse(this.responseText);
           var out = "";
           var i;
           for(i = 0; i < myArr.length; i++) {
               out += '<p>' + JSON.stringify(myArr[i]); + '</p>'
           }
           document.getElementById("msg").innerHTML = out;
        }
    };
    xhttp.open("GET", url, true);
    xhttp.send();
};







