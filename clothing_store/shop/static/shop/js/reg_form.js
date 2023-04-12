$('.modal__signin-sign-up.hoverable').on('click', function () {
                        $('.modal.modal__signup.enter-done').addClass('active');

                    });
                    $('.modal__signin-sign-up.hoverable').on('click', function () {
                        $('.modal__signin-tile.modal-tile').removeClass('active');

                    });
                    $('.icon.modal-close.icon__animated').on('click', function () {
                        $('.modal.modal__signup.enter-done').removeClass('active');

                    });
