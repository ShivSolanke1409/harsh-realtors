from django.contrib import admin
from .models import Property, Enquiry

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'property_type', 'location', 'area_sqft')
    list_filter = ('property_type', 'location')
    search_fields = ('title', 'location')

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('name', 'phone')


