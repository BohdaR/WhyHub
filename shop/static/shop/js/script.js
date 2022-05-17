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

    //Меню бургер
    const isMobile = {
      Android: function () {
        return navigator.userAgent.match(/Android/i);
      },
      BlackBerry: function () {
        return navigator.userAgent.match(/BlackBerry/i);
      },
      IOS: function () {
        return navigator.userAgent.match(/iPhone|iPad|iPod/i);
      },
      Opera: function () {
        return navigator.userAgent.match(/Opera/i);
      },
      Windows: function () {
        return navigator.userAgent.match(/Windows/i);
      },
      any: function () {
        return (
          isMobile.Android() | isMobile.BlackBerry() ||
          isMobile.IOS() ||
          isMobile.Opera() ||
          isMobile.Windows()
        );
      },
    };

    if (isMobile.any()) {
      document.body.classList.add("_pc");
    } else {
      document.body.classList.add("_touch");

      let menuArrows = document.querySelectorAll(".menu_arrow");
      if (menuArrows.length > 0) {
        for (let index = 0; index < menuArrows.length; index++) {
          const menuArrow = menuArrows[index];
          menuArrow.addEventListener("click", function (e) {
            menuArrow.parentElement.classList.toggle("_active");
          });
        }
      }
    }

const menuBody = document.querySelector(".menu_body");
const iconMenu = document.querySelector(".menu_icon");
if (iconMenu) {
  iconMenu.addEventListener("click", function (e) {
    iconMenu.classList.toggle("_active");
    document.body.classList.toggle("_lock");
    menuBody.classList.toggle("_active");
  });
}
