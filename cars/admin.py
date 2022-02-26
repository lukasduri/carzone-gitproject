from django.contrib import admin
from .models import Car
from django.utils.html import format_html



class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.car_photo.url))

    thumbnail.short_description = 'PICTURE'

    list_display = ('id', 'car_title', 'thumbnail', 'city', 'color', 'model', 'body_style', 'fuel_type', 'is_featured')
    list_display_links = ('id', 'car_title','thumbnail')
    search_fields = ('car_title', 'city', 'color', 'model', 'body_style', 'fuel_type', 'is_featured')
    list_editable = ('is_featured',)

admin.site.register(Car, CarAdmin)

