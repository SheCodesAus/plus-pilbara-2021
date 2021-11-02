var slideIndex = 1;
document.addEventListener('DOMContentLoaded', (event) => {
  showSlides(slideIndex)
  setInterval(() => { 
    increase()
   }, 1000)
});

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

function increase(n=1) {
  showSlides(slideIndex += n); 
}

// Thumbnail image controls
function currentSlide(m) {
  n = (slideIndex+m);
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  // var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  // for (i = 0; i < dots.length; i++) {
  //     dots[i].className = dots[i].className.replace(" active", "");
  // }
  slides[slideIndex-1].style.display = "block";
  // dots[slideIndex-1].className += " active";
}

function onError() {
  console.log("failed");
  var errorImage = document.getElementById("slides");
  var link = document.getElementById("bio-container");
  link.classList.add("errorStateHidden");

}
