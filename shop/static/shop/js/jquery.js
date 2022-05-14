jQuery('<div class="quantity-nav"><button class="quantity-button quantity-up" type="submit">+</button><button class="quantity-button quantity-down" type="submit">-</button></div>').insertAfter('.quantity input');
    jQuery('.quantity').each(function() {
      var spinner = jQuery(this),
        input = spinner.find('input[type="number"]'),
        btnUp = spinner.find('.quantity-up'),
        btnDown = spinner.find('.quantity-down'),
        min = input.attr('min'),
        max = input.attr('max');

      btnUp.click(function() {
        var oldValue = parseFloat(input.val());
        if (oldValue >= max) {
          var newVal = oldValue;
        } else {
          var newVal = oldValue + 1;
        }
        spinner.find("input").val(newVal);
        spinner.find("input").trigger("change");
      });

      btnDown.click(function() {
        var oldValue = parseFloat(input.val());
        if (oldValue <= min) {
          var newVal = oldValue;
        } else {
          var newVal = oldValue - 1;
        }
        spinner.find("input").val(newVal);
        spinner.find("input").trigger("change");
      });

    });
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