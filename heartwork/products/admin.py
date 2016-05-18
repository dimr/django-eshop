from django.contrib import admin
import os
# Register your models here.
from .models import Product, ProductImage
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import AdminFileWidget
from  django.forms import ModelForm


#http://stackoverflow.com/questions/10045064/django-admin-inline
class ProductImageInlineAdmin(admin.TabularInline):
    # fieldsets = (
    #     (
    #         None,
    #         {
    #             'fields': ('product', 'image',)
    #         }),)

    model = ProductImage

    fields = ( 'name','image','main','image_url')
    readonly_fields = ['image_url']
    #template='tabular-new.html'
    extra = 3

    def image_url(self,obj):
        return mark_safe(u'<img src={t} width=10% height=10%/>'.format(t=obj.thumb()))


    image_url.allow_tags=True
    image_url.short_description = 'Thumb'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'time_stamp'
    search_fields = ['title', 'description']
    list_display = ['title', 'price', 'sales_price', 'active', 'updated']
    list_editable = ['price', 'active', 'sales_price']
    readonly_fields = ['updated', 'time_stamp']
    prepopulated_fields = {"slug": ('title',)}
    inlines = [ProductImageInlineAdmin, ]


    class Meta:
        model = Product

    def images(self, obj):
        print obj.pk
        # print obj.products.all()[1].image.url
        print Product.objects.get(pk=29).products.filter()
        # print obj.products.filter(pk=obj.pk).title
        temp = [i.image.url for i in Product.objects.get(pk=obj.pk).products.filter()]
        return mark_safe(u'<img src="%s" width=60 height=60/>') % temp



    def save_model(self, request, obj, form, change):
        if obj.price < obj.sales_price:
            messages.add_message(request, messages.ERROR, mark_safe(
                '<h3 style="background-color: #e74c3c;">Sales price cannot be higher than normal price</h3>'))
            return
        super(ProductAdmin, self).save_model(request, obj, form, change)


# @admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['name','product', 'main','updated', 'active', 'thumb']
    readonly_fields = ('large_pic',)
    list_editable=['main']


    class Meta:
        model = ProductImage


        


admin.site.register(ProductImage, ProductImageAdmin)
