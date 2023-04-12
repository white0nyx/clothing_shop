const switcher_currency_basket = document.getElementById('button-currency-id-basket');
$('.header-buttons button').on('click', function () {
    $('.modal__cart.modal').addClass('active');

    const total_to_purchase = document.getElementById('total-to-purchase');

    switcher_currency_basket.textContent = $('.button-currency').text();

    total_to_purchase.textContent = $('.item_total_price').text();
    
});
$('.modal__cart-continue-shopping-2 button').on('click', function () {
    $('.modal__cart.modal').removeClass('active');

});