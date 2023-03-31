$('.switcher-language button').on('click', function () {
    if (!$('.select-list-transition-language>.select-list').hasClass('active')) {
        $('.select-list-transition-language>.select-list').addClass('active');
    } else {
        $('.select-list-transition-language>.select-list').removeClass('active');
    }
});

$('.switcher-currency button').on('click', function () {
    if (!$('.select-list-transition-currency>.select-list').hasClass('active')) {
        $('.select-list-transition-currency>.select-list').addClass('active');
    } else {
        $('.select-list-transition-currency>.select-list').removeClass('active');
    }
});
