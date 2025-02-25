from django.contrib import admin
from .models import contactus
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "number", "project", "query_description")

# Register your models here.
admin.site.register(contactus,ContactUsAdmin)
