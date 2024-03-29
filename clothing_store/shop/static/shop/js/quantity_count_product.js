const counters = document.querySelectorAll('[data-counter]');

if (counters) {
    counters.forEach(counter => {
        counter.addEventListener('click', e => {
            const target = e.target;

            if (target.closest('.counter_button')) {
                if (target.closest('.counter').querySelector('input').value == '' && (target.classList.contains('counter_button_minus') || target.classList.contains('counter_button_plus'))) {
                    target.closest('.counter').querySelector('input').value = 0;
                }

                let value = parseInt(target.closest('.counter').querySelector('input').value);

                if (target.classList.contains('counter_button_plus')) {
                    value++;
                } else {
                    --value;
                }

                if (value <= 0) {
                    value = 0;
                    target.closest('.counter').querySelector('.counter_button_minus').classList.add('disabled')
                }else {
                    target.closest('.counter').querySelector('.counter_button_minus').classList.remove('disabled')
                }

                if (value >= 20) {
                    value = 20;
                    target.closest('.counter').querySelector('.counter_button_plus').classList.add('disabled')
                }else {
                    target.closest('.counter').querySelector('.counter_button_plus').classList.remove('disabled')
                }

                target.closest('.counter').querySelector('input').value = value;
            }
        })
    })
}