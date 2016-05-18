from django.contrib import admin
from clients.models import Client, ClientProfile


class ClientProfileInlineAdmin(admin.TabularInline):
    model = ClientProfile
    fields = ('address', 'country')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('_full_name', 'email',)
    list_display_links = ('_full_name', 'email',)
    readonly_fields = ('created',)
    inlines = [ClientProfileInlineAdmin, ]

    def _full_name(self, obj):
        '''
        Breaks ordering
        http://stackoverflow.com/questions/12048176/how-can-i-rename-a-column-label-in-django-admin-for-a-field-that-is-a-method-pr
        :param obj:
        :return:
        '''
        return obj.get_full_name

    _full_name.short_description = 'Full Name'
    _full_name.admin_order_field = 'first_name'


class ClientProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = ClientProfile


admin.site.register(Client, ClientAdmin)
# admin.site.register(ClientProfile, ClientProfileAdmin)
