from django.db import models
from django.db.models import Q
from mediastore.fields import MediaField, MultipleMediaField
from django.utils.translation import ugettext_lazy as _
import urllib
import urllib2
from django.core.files import File
import os
import re
import json

class FrontPage(models.Model):
    title = models.CharField(max_length="250", blank=True, null=True)
    description = models.CharField(max_length="250", blank=True, null=True)
    bgcolor = models.CharField(max_length="250", blank=True, null=True, help_text="HEX value", verbose_name="Background Colour")
    show_last = models.BooleanField(default=False, help_text="Shows the email address", verbose_name="Shows the Contact page")
    email_description = models.TextField(blank=True, null=True)
    email_title = models.CharField(max_length="250", blank=True, null=True)
    email_link = models.EmailField(blank=True, null=True)
    is_video = models.BooleanField(default=False)
    is_image = models.BooleanField(default=False)
    is_audio = models.BooleanField(default=False)
    slide_delay = models.PositiveIntegerField(blank=True, null=True)

    def __unicode__(self):
        return "Front Page Settings"

    class Meta:
        verbose_name = _(u'Front Page Settings')
        verbose_name_plural = _(u'Front Page Settings')

class ImageType(models.Model):
    title = models.CharField(max_length="250", blank=True, null=True)
    date = models.DateField(db_index=True, null=True, blank=True)
    description = models.CharField(max_length="250", blank=True, null=True)
    is_public = models.BooleanField(default=True, db_index=True, help_text='You can hide this item from site')
    sort_value = models.IntegerField(default=10, db_index=True, help_text='The order in which you want Work to appear when overriding date order')

    cover_image = MediaField(
        related_name='mediapage_image_cover',
        null=True, blank=True,
        limit_choices_to={'content_type__model':'image'}
        )

    detail_media = MultipleMediaField(sorted=True,
                                      null=True, blank=True,
                                      limit_choices_to={'content_type__model':'image'},
                                      related_name='mediapage_image_detail_media',
                                      help_text="If you have a production select it bellow if you want to create a new gallery use this methord. Image that appears in the gallery. Images will show at a height of 230px the gallery overlay images should be 900x575px")
    svg = models.FileField(upload_to='svg/', blank=True, null=True)

    def __unicode__(self):
        if self.title is not '&nbsp':
            return self.title
        else:
            return 'Image Gallery'

    class Meta:
        verbose_name = _(u'Images')
        verbose_name_plural = _(u'Images')
        ordering = ('sort_value',)


class AudioType(models.Model):
    title = models.CharField(max_length="250", blank=True, null=True)
    is_public = models.BooleanField(default=True, db_index=True, help_text='You can hide this item from site')
    sort_value = models.IntegerField(default=10, db_index=True, help_text='The order in which you want Work to appear when overriding date order')
    track = MediaField(
        null=True, blank=True,
        related_name='media_audio_track',
        limit_choices_to={'content_type__model':'embeded'},
        help_text="Audio tracks from sound cloud embeds"
    )

    def __unicode__(self):
        if self.title is not '&nbsp':
            return self.title
        else:
            return 'Audio'

    class Meta:
        verbose_name = _(u'Audio')
        verbose_name_plural = _(u'Audio')
        ordering = ('sort_value',)


class FilmType(models.Model):
    title = models.CharField(max_length="250", blank=True, null=True)
    is_public = models.BooleanField(default=True, db_index=True, help_text='You can hide this item from site')
    date = models.DateField(db_index=True, blank=True, null=True)
    description = models.CharField(max_length="250", blank=True, null=True)
    sort_value = models.IntegerField(default=10, db_index=True, help_text='The order in which you want Work to appear when overriding date order')
    video = MediaField(
        null=True, blank=True,
        related_name='media_film_video',
        limit_choices_to={'content_type__model':'embeded'},
        help_text="Film video from youtube"
    )
    video_url = models.TextField(blank=True, null=True, help_text='Use for url of youtube or vimeo videos.')
    video_thumb = MediaField(
        null=True, blank=True,
        related_name='media_film_videourl_image',
        limit_choices_to={'content_type__model':'image'},
        help_text="Image for video"
    )
    video_url_thumb = models.ImageField(upload_to='ourmediaimages', null=True, blank=True)

    def __unicode__(self):
        if self.title is not '&nbsp':
            return self.title
        else:
            return 'Film'

    def save(self, *args, **kwargs):
        super(FilmType, self).save(*args, **kwargs)
        get_remote_image(self)

    class Meta:
        verbose_name = _(u'Film')
        verbose_name_plural = _(u'Film')
        ordering = ('sort_value',)

def get_remote_image(self):
    if self.video_url and not self.video_url_thumb:
        if 'youtube' in self.video_url:
            #get youtube image
            ar = self.video_url.split("=",1)[1]
            url = 'http://img.youtube.com/vi/{0}/hqdefault.jpg'.format(ar)
            result = urllib.urlretrieve(url)
            self.video_url_thumb.save(os.path.basename(ar),File(open(result[0])))
            self.save()
        elif 'vimeo' in self.video_url:
            ar = re.findall(r'\b\d+\b',self.video_url)[0]
            url = 'http://vimeo.com/api/v2/video/{0}.json'.format(ar)
            result = urllib2.urlopen(url)
            jn = json.loads(result.read())
            img = urllib.urlretrieve(jn[0][u'thumbnail_large'])
            self.video_url_thumb.save(os.path.basename(ar),File(open(img[0])))
            self.save()
            print result
