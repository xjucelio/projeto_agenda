from django.contrib import admin
from contact import models

# Register your models here.


@admin.register(models.Contact)  # type: ignore
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone',
    ordering = '-id',
    # list_filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 10
    list_max_show_all = 200
    # list_editable = 'first_name', 'last_name',
    list_display_links = 'id', 'phone',


@admin.register(models.Category)  # type: ignore
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',
