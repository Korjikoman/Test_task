from django.contrib import admin
from .models import Places, PlaceImage
from django.utils.html import format_html
from django.urls import reverse
from django.http import HttpResponse
import os

class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 1
    readonly_fields = ['image_preview', 'download_link']
    
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" height="100" style="object-fit: cover;" />',
                obj.image.url
            )
        return "No image"
    image_preview.short_description = 'Preview'
    
    def download_link(self, obj):
        if obj.image:
            return format_html(
                '<a href="{}" download class="button">📥 Download</a>',
                obj.image.url
            )
        return "No image"
    download_link.short_description = 'Download'

@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_date', 'images_count', 'images_preview']
    list_filter = ['created_date', 'author']
    search_fields = ['title', 'description_short']
    inlines = [PlaceImageInline]
    readonly_fields = ['coordinates_display']
    
    def images_count(self, obj):
        return obj.images.count()
    images_count.short_description = 'Images Count'
    
    def images_preview(self, obj):
        images = obj.images.all()[:2]
        previews = []
        for img in images:
            if img.image:
                previews.append(
                    f'<img src="{img.image.url}" width="50" height="50" style="object-fit: cover; margin-right: 5px;" />'
                )
        return format_html(''.join(previews)) if previews else "No images"
    images_preview.short_description = 'Images Preview'
    
    def coordinates_display(self, obj):
        return format_html(
            '<strong>Longitude:</strong> {}<br><strong>Latitude:</strong> {}',
            obj.lng, obj.lat
        )
    coordinates_display.short_description = 'Coordinates'
    

    fieldsets = (
        ('Основная информация', {
            'fields': ('author', 'title', 'description_short', 'description_long')
        }),
        ('Координаты', {
            'fields': ('lng', 'lat', 'coordinates_display')
        }),
    )


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    list_display = ['place', 'image_preview', 'download_link', 'order']
    list_editable = ['order']
    readonly_fields = ['image_preview', 'download_link', 'file_info']
    list_display_links = ['place']
    
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" height="100" style="object-fit: cover;" />',
                obj.image.url
            )
        return "No image"
    image_preview.short_description = 'Preview'
    
    def download_link(self, obj):
        if obj.image:
            return format_html(
                '<a href="{}" download="{}" class="button">📥 Download</a>',
                obj.image.url,
                os.path.basename(obj.image.name)
            )
        return "No image"
    download_link.short_description = 'Download'
    
    def file_info(self, obj):
        if obj.image:
            return format_html(
                '<strong>File name:</strong> {}<br>'
                '<strong>Size:</strong> {}<br>'
                '<strong>Path:</strong> {}',
                os.path.basename(obj.image.name),
                self.get_file_size(obj.image.size),
                obj.image.name
            )
        return "No file info"
    file_info.short_description = 'File Information'
    
    def get_file_size(self, size):
        """Конвертирует размер файла в читаемый формат"""
        for unit in ['bytes', 'KB', 'MB', 'GB']:
            if size < 1024.0:
                return f"{size:.1f} {unit}"
            size /= 1024.0
        return f"{size:.1f} TB"
    
    fieldsets = (
        (None, {
            'fields': ('place', 'order')
        }),
        ('Image', {
            'fields': ('image', 'image_preview', 'download_link', 'file_info')
        }),
    )