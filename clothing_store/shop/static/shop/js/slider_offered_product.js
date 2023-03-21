let offset2 = 0;
const sliderLine2 = document.querySelector('.slide-line2');

document.querySelector('.slider-next2').addEventListener('click', function(){
    offset2 = offset2 + 362;
    if (offset2 > 1810) {
        offset2 = 0;
    }
    sliderLine2.style.left = -offset2 + 'px';
});

document.querySelector('.slider-prev2').addEventListener('click', function () {
    offset2 = offset2 - 362;
    if (offset2 < 0) {
        offset2 = 1810;
    }
    sliderLine2.style.left = -offset2 + 'px';
});