from django.contrib import admin

from home.models import Antrenor, Images, Setting


admin.site.register(Setting)


class AntrenorImagesInline(admin.TabularInline):
    model = Images
    extra = 5
    readonly_fields = ('image_tag',)
class AntrenorAdmin(admin.ModelAdmin):
    # fields = ['title', 'status'] == 
    list_display = ['title','image_tag']
    list_filter = ['status']
    readonly_fields = ('image_tag',) 
    inlines = [AntrenorImagesInline]
admin.site.register(Antrenor, AntrenorAdmin)

class ImagesAdmin(admin.ModelAdmin):
    # fields = ['title', 'status']
    list_display = ['title','antrenor', 'image_tag']
admin.site.register(Images, ImagesAdmin)