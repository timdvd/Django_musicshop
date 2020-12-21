window.addEventListener('load', () => {
    let mask = document.querySelector('.mask');
    mask.classList.add('hide');
    setTimeout(() => {
        mask.remove();
    },600);
});

let btnTop = $('.btn-top');
$(window).on('scroll', function(){
    if ($(window).scrollTop() >= 80){
        btnTop.fadeIn();
    }else{
        btnTop.fadeOut();
    }
});

btnTop.on('click', function(){
   $('html,body').animate({scrollTop:0},900); 
});

$(document).ready(function(){
    $('.sidebarBtn').click(function(){
      $('.sidebar').toggleClass('active');
      $('.sidebarBtn').toggleClass('toggle');
    });
  });
  
  $('.pretty').click(function(){
    $(this).toggleClass('pretty-active');
});
$(document).ready(function(){
    $('.arrivals-slider').slick({
        slidesToShow: 4,
        slidesToScroll: 4,
        dots: false,
        arrows: true,
        responsive: [
            {
                breakpoint: 1080,
                settings: {
                  slidesToShow: 3,
                  slidesToScroll: 3,
                }
              },
          {
            breakpoint: 992,
            settings: {
              slidesToShow: 3,
              slidesToScroll: 3,
            }
          },
          {
            breakpoint: 925,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 2,
            }
          },
            {
                breakpoint: 676,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                }
            },
        ]
      });
});

$(document).ready(function(){
    $('.albums-slider').slick({
        slidesToShow: 4,
        slidesToScroll: 4,
        dots: false,
        arrows: true,
        responsive: [
            {
                breakpoint: 1080,
                settings: {
                  slidesToShow: 3,
                  slidesToScroll: 3,
                }
              },
          {
            breakpoint: 992,
            settings: {
              slidesToShow: 3,
              slidesToScroll: 3,
            }
          },
          {
            breakpoint: 925,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 2,
            }
          },
            {
                breakpoint: 676,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                }
            },
        ]
      });
});

$(document).ready(function(){
  $('.publishers-slider').slick({
      slidesToShow: 6,
      slidesToScroll: 6,
      dots: false,
      arrows: true,
      responsive: [
          {
              breakpoint: 1080,
              settings: {
                slidesToShow: 6,
                slidesToScroll: 6,
              }
            },
        {
          breakpoint: 992,
          settings: {
            slidesToShow: 5,
            slidesToScroll: 5,
          }
        },
        {
          breakpoint: 925,
          settings: {
            slidesToShow: 4,
            slidesToScroll: 4,
          }
        },
        {
          breakpoint: 767,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 3,
          }
        },
          {
              breakpoint: 676,
              settings: {
                  slidesToShow: 3,
                  slidesToScroll: 3,
              }
          },
          {
            breakpoint: 565,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 2,
            }
        },
          {
              breakpoint: 480,
              settings: {
                  slidesToShow: 2,
                  slidesToScroll: 2,
              }
          },
          {
            breakpoint: 380,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
            }
        },
      ]
    });
});