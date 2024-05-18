from django.contrib import admin
from places.models import Category, Place, Gellery


class GalleryAdmin(admin.TabularInline):
    list_display = ["featured_image", "place"]
    model = Gellery

class PlaceAdmin(admin.ModelAdmin):
    list_display = ["name", "location", "category"]
    inlines = [GalleryAdmin]
admin.site.register(Place, PlaceAdmin)



admin.site.register(Category)
