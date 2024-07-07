class DefaultCurrencyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and 'temporary_currency' not in request.session:
            request.session['temporary_currency'] = 'RUB'
        return self.get_response(request)