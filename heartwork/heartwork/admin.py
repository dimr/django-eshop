# __author__ = 'dimitris'
from django.contrib import admin
from django.utils.translation import ugettext_lazy
from products.models import Product, ProductImage
from products.admin import ProductAdmin, ProductImageAdmin
from clients.models import Client, ClientProfile
from clients.admin import ClientAdmin, ClientProfileAdmin


class HeartworkAdmin(admin.AdminSite):
    site_header = ugettext_lazy("Heartwork")
    site_title = ugettext_lazy('heart admin')
    index_title = ugettext_lazy('Administration')


admin_site = HeartworkAdmin(name='the_admin')
admin_site.register(Product, ProductAdmin)
admin_site.register(ProductImage, ProductImageAdmin)
admin_site.register(Client, ClientAdmin)
admin.site.register(ClientProfile,ClientProfileAdmin)
