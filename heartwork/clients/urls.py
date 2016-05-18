try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

from views import RegistrationView, LoginView, ProfileDetailView

# place app url patterns here


urlpatterns = patterns('',
                       url(r'/login/$', LoginView.as_view(), name='login'),
                       url(r'/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/products/'},
                           name='auth_logout'),
                       url(r'/register/$', RegistrationView.as_view(), name='register'),
                       url(r'/profile/(?P<uuid>[^/]+)/$', ProfileDetailView.as_view(), name='detailed_profile'),
                       )
