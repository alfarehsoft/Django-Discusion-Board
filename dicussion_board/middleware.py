from django.conf import settings
from django.urls import resolve
from django.utils import translation

class PathBasedLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        language_code=request.LANGUAGE_CODE
        # Activate language
        translation.activate(language_code)
        request.LANGUAGE_CODE = translation.get_language()
        # Call the next middleware or view
        response = self.get_response(request)
        return response