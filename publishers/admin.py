from django.contrib import admin
from .models import Publisher
# Register your models here.

class PublisherAdmin(admin.ModelAdmin):
    search_fields = ['name', 'timestamp']
    list_display = ['name', 'timestamp', 'active']
    list_editable = ['active']
    class Meta:
        model = Publisher

admin.site.register(Publisher, PublisherAdmin)
