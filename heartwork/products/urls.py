__author__ = 'dimitris'

from django.conf.urls import patterns, url
from views import SingleProductView, AllProductsView, PicList
from django.views.generic import TemplateView
import views

urlpatterns = patterns(
    '',
    url(r'^$', AllProductsView.as_view(), name='all-products'),
    url(r'(?P<slug>[\w-]*)/pics/', PicList.as_view()),
    url(r'(?P<slug>[\w-]*)/$', SingleProductView.as_view(), name='single_product'),

)
