from django import forms
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from mediastore.admin import ModelAdmin
from mediastore.models import Media
from .models import *


class FrontPageAdminForm(ModelAdmin):
    list_display = ('title',)
    save_on_top = True


class ImageAdmin(ModelAdmin):
    list_display = ('title','sort_value','is_public',)
    list_editable = ('sort_value', 'is_public',)
    fieldsets = (
        (_('General'),{
            'classes':('wide',),
            'fields':(
                'title',
                'sort_value',
                'is_public',
            ),
        }),
        (_('Gallery'),{
            'classes':('wide',),
            'fields':(
                'description',
                'date',
                'cover_image',
                'detail_media',
                'svg',
            ),
        }),
    )

class AudioAdmin(ModelAdmin):
    list_display = ('title','sort_value','is_public',)
    list_editable = ('sort_value', 'is_public',)

class FilmAdmin(ModelAdmin):
    list_display = ('title','sort_value','is_public',)
    list_editable = ('sort_value', 'is_public',)
    fields = ('title','is_public','date','description','sort_value','video','video_url','video_url_thumb')

admin.site.register(FrontPage, FrontPageAdminForm)
admin.site.register(ImageType, ImageAdmin)
admin.site.register(AudioType, AudioAdmin)
admin.site.register(FilmType, FilmAdmin)
