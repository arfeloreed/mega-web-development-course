// var fName = document.getElementById("fname");
// var lName = document.getElementById("lname");
// var btn = document.getElementById("btn");
// var displayName = document.getElementById("display-name");

// function print() {
//     // console.log(fName.value + " " + lName.value)
//     displayName.textContent = fName.value + " " + lName.value;
// }
// // btn.addEventListener("click", print);


var btn = document.getElementById("btn");
var displayName = document.getElementById("display-name");

function DisplayName(firstname, lastname) {
    this.firstName = firstname;
    this.lastName = lastname;
}
function getName() {
    var fName = document.getElementById("fname");
    var lName = document.getElementById("lname");

    var user = new DisplayName(fName.value, lName.value);
    displayName.textContent = user.firstName + " " + user.lastName;
}

btn.addEventListener("click", getName);