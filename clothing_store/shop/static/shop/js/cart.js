const switcher_currency_basket = document.getElementById('button-currency-id-basket');
$('.header-buttons button').on('click', function () {
                    $('.modal__cart.modal').addClass('active');
                    switcher_currency_basket.textContent = $('.button-currency').text()
                    
                });
$('.modal__cart-continue-shopping-2 button').on('click', function () {
    $('.modal__cart.modal').removeClass('active');

});