from oscar.apps.customer.views import LogoutView as CoreLogoutView
from django.conf import settings
from django.contrib.auth import logout as auth_logout

class LogoutView(CoreLogoutView):
    url = settings.LOGOUT_REDIRECT_URL
    permanent = False

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        response = super().get(request, *args, **kwargs)

        for cookie in settings.OSCAR_COOKIES_DELETE_ON_LOGOUT:
            response.delete_cookie(cookie)

        return response
