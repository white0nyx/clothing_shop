let offset = 0;
const sliderLine = document.querySelector('.slide-line');

document.querySelector('.slider-next').addEventListener('click', function(){
    offset = offset + 362;
    if (offset > 724) {
        offset = 0;
    }
    sliderLine.style.left = -offset + 'px';
});

document.querySelector('.slider-prev').addEventListener('click', function () {
    offset = offset - 362;
    if (offset < 0) {
        offset = 724;
    }
    sliderLine.style.left = -offset + 'px';
});

