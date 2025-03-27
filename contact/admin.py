from django.contrib import admin
from contact import models

# Register your models here. admin.ModelAdmin

@admin.register(models.Contact)
class contactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'show',
    ordering = '-id',
    # list_filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 10
    list_max_show_all = 200         
    list_editable = 'first_name', 'last_name', 'show',
    list_display_links = 'phone','id',
    
@admin.register(models.Category)
class categoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',
