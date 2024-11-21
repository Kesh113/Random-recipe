class EnsureSessionMiddleware:
    """Создание сессии для анонимного пользователя"""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Проверяем, есть ли уже session_key
        if not request.session.session_key:
            # Устанавливаем временное значение, чтобы сессия сохранилась
            request.session['is_active'] = True
        # Устанавливаем время действия сессии
        request.session.set_expiry(14 * 24 * 3600)
        response = self.get_response(request)
        return response
