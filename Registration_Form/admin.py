from django.contrib import admin

# Register your models here.
from .models import Registration

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ("id", "company_name", "establishment_year", "company_pan", "company_gst")
    search_fields = ("company_name", "company_pan", "company_gst", "state")


admin.site.register(Registration, RegistrationAdmin)