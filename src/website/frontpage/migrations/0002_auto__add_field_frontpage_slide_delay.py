# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'FrontPage.slide_delay'
        db.add_column(u'frontpage_frontpage', 'slide_delay',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'FrontPage.slide_delay'
        db.delete_column(u'frontpage_frontpage', 'slide_delay')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'frontpage.audiotype': {
            'Meta': {'ordering': "('sort_value',)", 'object_name': 'AudioType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'sort_value': ('django.db.models.fields.IntegerField', [], {'default': '10', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': "'250'", 'null': 'True', 'blank': 'True'}),
            'track': ('mediastore.fields.related.MediaField', [], {'blank': 'True', 'related_name': "'media_audio_track'", 'null': 'True', 'to': "orm['mediastore.Media']"})
        },
        u'frontpage.filmtype': {
            'Meta': {'ordering': "('sort_value',)", 'object_name': 'FilmType'},
            'date': ('django.db.models.fields.DateField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': "'250'", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'sort_value': ('django.db.models.fields.IntegerField', [], {'default': '10', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': "'250'", 'null': 'True', 'blank': 'True'}),
            'video': ('mediastore.fields.related.MediaField', [], {'blank': 'True', 'related_name': "'media_film_video'", 'null': 'True', 'to': "orm['mediastore.Media']"}),
            'video_thumb': ('mediastore.fields.related.MediaField', [], {'blank': 'True', 'related_name': "'media_film_videourl_image'", 'null': 'True', 'to': "orm['mediastore.Media']"}),
            'video_url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'video_url_thumb': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'frontpage.frontpage': {
            'Meta': {'object_name': 'FrontPage'},
            'bgcolor': ('django.db.models.fields.CharField', [], {'max_length': "'250'", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': "'250'", 'null': 'True', 'blank': 'True'}),
            'email_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email_link': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'email_title': ('django.db.models.fields.CharField', [], {'max_length': "'250'", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_audio': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_image': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_video': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'show_last': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slide_delay': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': "'250'", 'null': 'True', 'blank': 'True'})
        },
        u'frontpage.imagetype': {
            'Meta': {'ordering': "('sort_value',)", 'object_name': 'ImageType'},
            'cover_image': ('mediastore.fields.related.MediaField', [], {'blank': 'True', 'related_name': "'mediapage_image_cover'", 'null': 'True', 'to': "orm['mediastore.Media']"}),
            'date': ('django.db.models.fields.DateField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': "'250'", 'null': 'True', 'blank': 'True'}),
            'detail_media': ('mediastore.fields.related.MultipleMediaField', [], {'blank': 'True', 'related_name': "'mediapage_image_detail_media'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['mediastore.Media']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'sort_value': ('django.db.models.fields.IntegerField', [], {'default': '10', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': "'250'", 'null': 'True', 'blank': 'True'})
        },
        'mediastore.media': {
            'Meta': {'ordering': "('created',)", 'object_name': 'Media'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'blank': 'True'})
        },
        u'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'taggit.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_tagged_items'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_items'", 'to': u"orm['taggit.Tag']"})
        }
    }

    complete_apps = ['frontpage']