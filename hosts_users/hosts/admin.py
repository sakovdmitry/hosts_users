from django.contrib import admin

from .models import Hosts


class HostsAdmin(admin.ModelAdmin):
    list_display = ('ip', 'port', 'resource', 'owner', 'date')
    search_fields = ('owner',)
    list_filter = ('date',)


admin.site.register(Hosts, HostsAdmin)
