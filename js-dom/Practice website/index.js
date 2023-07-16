// var btn = document.querySelector("#intro a")
// console.log(btn)
// btn.style.boxShadow="0 5px 20px #000"

// put a box shadow on a button
// document.querySelector("#intro a").style.boxShadow="0 5px 20px #000"


//  create a function that hides the main nav when the button is clicked.
// function hideNav() {
//     document.querySelector(".main-nav").style.display="none";
// }

// create an overlay review
function showReview() {
    // document.querySelector(".review-overlay").style.opacity="1";
    // document.querySelector(".product-img").style.filter="brightness(0.4)";
    // document.querySelector(".review-overlay").classList.add("overlay-hover");
    // document.querySelector(".product-img").classList.add("img-hover");
    document.querySelector(".review-overlay").classList.toggle("overlay-hover");
    document.querySelector(".product-img").classList.toggle("img-hover");
}

function hideReview() {
    // document.querySelector(".review-overlay").style.opacity="0";
    // document.querySelector(".product-img").style.filter="brightness(1)";
    // document.querySelector(".review-overlay").classList.remove("overlay-hover");
    // document.querySelector(".product-img").classList.remove("img-hover");
    document.querySelector(".review-overlay").classList.toggle("overlay-hover");
    document.querySelector(".product-img").classList.toggle("img-hover");
}

// do the same thing with event listener
var productImg = document.querySelector(".product-img");

productImg.addEventListener("mouseover", showReview);
productImg.addEventListener("mouseout", hideReview);


// toggle darkmode
var sun = document.getElementById("sun-icon");
var moon = document.getElementById("moon-icon");

function darkMode() {
    sun.style.display="none";
    moon.style.display="block";
    document.querySelector("body").classList.toggle("body");
    document.querySelector("#intro p").style.color="#EEF0EB";
}

function lightMode() {
    sun.style.display="block";
    moon.style.display="none";
    document.querySelector("body").classList.toggle("body");
    document.querySelector("#intro p").style.color="#3c404a";
}


// listen to video and make a function that prints in the console if the video ended
function videoEnded() {
    console.log("Video has ended.");
}

var vid = document.querySelector("#intro video");
// console.log(vid)
vid.addEventListener("ended", videoEnded);