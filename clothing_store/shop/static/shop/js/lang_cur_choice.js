$('.switcher-language button').on('click', function () {
    if (!$('.select-list-transition-language>.select-list').hasClass('active')) {
        $('.select-list-transition-language>.select-list').addClass('active');
        
    } else {
        $('.select-list-transition-language>.select-list').removeClass('active');
    }
});


const switcher_language = document.getElementById('button-language-id');

ENG.addEventListener('click', function handleClick() {
    switcher_language.textContent = "АНГЛ"
    $('.select-list-transition-language>.select-list').removeClass('active');
  });

RUS.addEventListener('click', function handleClick() {
    switcher_language.textContent = "РУС"
    $('.select-list-transition-language>.select-list').removeClass('active');
});

UKR.addEventListener('click', function handleClick() {
    switcher_language.textContent = "УКР"
    $('.select-list-transition-language>.select-list').removeClass('active');
});




$('.switcher-currency button').on('click', function () {
    if (!$('.select-list-transition-currency>.select-list').hasClass('active')) {
        $('.select-list-transition-currency>.select-list').addClass('active');
    } else {
        $('.select-list-transition-currency>.select-list').removeClass('active');
    }
});

const switcher_currency = document.getElementById('button-currency-id');


USD.addEventListener('click', function handleClick() {
    switcher_currency.textContent = "USD"
    
    $('.select-list-transition-language>.select-list').removeClass('active');
  });

EUR.addEventListener('click', function handleClick() {
    switcher_currency.textContent = "EUR"
    $('.select-list-transition-currency>.select-list').removeClass('active');
  });

UAH.addEventListener('click', function handleClick() {
    switcher_currency.textContent = "UAH"
    $('.select-list-transition-currency>.select-list').removeClass('active');
  });
KZT.addEventListener('click', function handleClick() {
    switcher_currency.textContent = "KZT"
    $('.select-list-transition-currency>.select-list').removeClass('active');
  }); 
CZK.addEventListener('click', function handleClick() {
    switcher_currency.textContent = "CZK"
    $('.select-list-transition-currency>.select-list').removeClass('active');
  }); 
PLN.addEventListener('click', function handleClick() {
    switcher_currency.textContent = "PLN"
    $('.select-list-transition-currency>.select-list').removeClass('active');
  });
GEL.addEventListener('click', function handleClick() {
    switcher_currency.textContent = "GEL"
    $('.select-list-transition-currency>.select-list').removeClass('active');
  });
RUB.addEventListener('click', function handleClick() {
    switcher_currency.textContent = "RUB"
    $('.select-list-transition-currency>.select-list').removeClass('active');
  });