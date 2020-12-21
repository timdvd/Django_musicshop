from django.contrib import admin
from .models import GuestEmail, Profile
# Register your models here.

class UserAdmin():
    pass

class GuestEmailAdmin(admin.ModelAdmin):
    search_fields = ['email']
    list_display = ['email', 'active', 'timestamp']
    class Meta:
        model = GuestEmail

admin.site.register(Profile)
admin.site.register(GuestEmail, GuestEmailAdmin)
