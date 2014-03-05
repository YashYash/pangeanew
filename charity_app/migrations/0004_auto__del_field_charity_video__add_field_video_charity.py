# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Charity.video'
        db.delete_column(u'charity_app_charity', 'video_id')

        # Adding field 'Video.charity'
        db.add_column(u'charity_app_video', 'charity',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['charity_app.Charity']),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Charity.video'
        raise RuntimeError("Cannot reverse this migration. 'Charity.video' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Charity.video'
        db.add_column(u'charity_app_charity', 'video',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['charity_app.Video']),
                      keep_default=False)

        # Deleting field 'Video.charity'
        db.delete_column(u'charity_app_video', 'charity_id')


    models = {
        u'charity_app.charity': {
            'Meta': {'object_name': 'Charity'},
            'charity_url': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'charity_app.video': {
            'Meta': {'object_name': 'Video'},
            'charity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['charity_app.Charity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'video_url': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        }
    }

    complete_apps = ['charity_app']