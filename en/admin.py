from django.contrib import admin
from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'author')
    list_filter = ('title', 'pub_date', 'author')
    fields = ['title', 'text', 'pub_date', 'image', 'author']
    # exclude = ('pub_date',)
    date_hierarchy = 'pub_date'
    actions_on_bottom = True

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'price', 'author')
    list_filter = ('name', 'status', 'author')
    fieldsets = (
    ('Your Text', {'fields': ('name', 'info', 'link')}),
    ('Your Text', {'fields': ('status', 'price', 'author')}),
    )
    actions_on_bottom = True
