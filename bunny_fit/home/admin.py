from django.contrib import admin

from home.models import Antrenor, Fiyatlar, Images, Setting


admin.site.register(Setting)


class AntrenorImagesInline(admin.TabularInline):
    model = Images
    extra = 5
    readonly_fields = ('image_tag',)
class AntrenorAdmin(admin.ModelAdmin):
    # fields = ['name', 'status'] == 
    list_display = ['name','keywords','detail','image_tag','status']
    list_filter = ['status']
    readonly_fields = ('image_tag',) 
    inlines = [AntrenorImagesInline]
admin.site.register(Antrenor, AntrenorAdmin)

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['name','antrenor', 'image_tag']
admin.site.register(Images, ImagesAdmin)

class FiyatlarAdmin(admin.ModelAdmin):
    list_display = ['paket','ay','odeme_sekli','price','detail','status']
    list_filter = ['status']
admin.site.register(Fiyatlar, FiyatlarAdmin)