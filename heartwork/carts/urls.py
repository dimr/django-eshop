from django.conf.urls import patterns, url
from .views import view, update_cart

urlpatterns = patterns(
    '',

    url(r'^$', view, name='cart'),
    url(r'(?P<slug>[\w-]*)/$', update_cart, name='update_the_cart'),
)
