let slides = document.querySelectorAll('.slide-img');
let Left = document.getElementsByClassName('Left');
let Right = document.getElementsByClassName('Right');
let i = 0


console.log(0)
slides[0].style.opacity = 1;


function left_next_slide() {
  slides[i].style.opacity = 0;
  i++;
  if (i === slides.length) {
    i = 0;
  }
  slides[i].style.opacity = 1;
}

function right_next_slide() {
  slides[i].style.opacity = 0;
  if (i === 0) {
    i = slides.length;
  }
  i--;
  console.log(i)
  slides[i].style.opacity = 1;
}

Left[0].addEventListener("click", left_next_slide);
Right[0].addEventListener("click", right_next_slide);
