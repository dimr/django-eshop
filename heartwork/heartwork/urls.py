from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
# from admin import HeartworkAdmin
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from admin import admin_site
from  products.views import AllProductsView, HomeView
from django.http import HttpResponse

admin.autodiscover()

urlpatterns = patterns('',

                       url(r'^robots.txt', lambda x: HttpResponse("User-Agent: *\nDisallow:", content_type="text/plain"), name="robots_file"),
                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^$', HomeView.as_view(), name='go-to-home'),
                       url(r'^admin/', include(admin.site.urls)),

                       url(r'products/', include('products.urls')),
                       url(r'about/$', TemplateView.as_view(template_name='about.html'), name='about-page'),
                       url(r'^clients', include('clients.urls')),
                       url(r'^cart/', include('carts.urls')),
                       )

# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                                'document_root': settings.MEDIA_ROOT}))
