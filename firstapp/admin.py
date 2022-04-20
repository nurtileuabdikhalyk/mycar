from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Vehicle, Service, Reviews, Blog, Exterior, Character, VehicleShots


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'lugage', 'year', 'preview')
    prepopulated_fields = {'slug': ('name',), }
    list_filter = ('name', 'year', 'minimum_age')
    search_fields = ('name', 'year', 'description')

    def preview(self, obj):
        return mark_safe(f"<img src='{obj.image.url}' style='width:100px;height:60px;'>")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',), }


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email')
    list_display_links = ('name', 'surname',)
    search_fields = ('name', 'surname', 'email')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'data')
    search_fields = ('title',)
    list_filter = ('title', 'data')


@admin.register(VehicleShots)
class VehicleShotsAdmin(admin.ModelAdmin):
    readonly_fields = ('preview',)
    fields = ('title', 'description', 'vehicle', 'image', 'preview')

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')


admin.site.register(Exterior)
admin.site.register(Character)
admin.site.site_title = "NurCar"
admin.site.site_header = "NurCar"
