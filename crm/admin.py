from django.contrib import admin
from .models import Contact, Deal

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'company', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'company')

@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ('title', 'contact', 'value', 'stage', 'assigned_to', 'created_at')
    list_filter = ('stage',)
    search_fields = ('title', 'contact__first_name', 'contact__last_name')
