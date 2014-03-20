# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Giver.slogan'
        db.add_column(u'giver_app_giver', 'slogan',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True),
                      keep_default=False)

        # Adding field 'Giver.cover_photo'
        db.add_column(u'giver_app_giver', 'cover_photo',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True),
                      keep_default=False)

        # Adding field 'Giver.video_url'
        db.add_column(u'giver_app_giver', 'video_url',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True),
                      keep_default=False)


        # Changing field 'Giver.name'
        db.alter_column(u'giver_app_giver', 'name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Giver.giver_url'
        db.alter_column(u'giver_app_giver', 'giver_url', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True))

        # Changing field 'Giver.image'
        db.alter_column(u'giver_app_giver', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

        # Changing field 'Giver.description'
        db.alter_column(u'giver_app_giver', 'description', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True))

    def backwards(self, orm):
        # Deleting field 'Giver.slogan'
        db.delete_column(u'giver_app_giver', 'slogan')

        # Deleting field 'Giver.cover_photo'
        db.delete_column(u'giver_app_giver', 'cover_photo')

        # Deleting field 'Giver.video_url'
        db.delete_column(u'giver_app_giver', 'video_url')


        # User chose to not deal with backwards NULL issues for 'Giver.name'
        raise RuntimeError("Cannot reverse this migration. 'Giver.name' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Giver.name'
        db.alter_column(u'giver_app_giver', 'name', self.gf('django.db.models.fields.CharField')(max_length=200))

        # User chose to not deal with backwards NULL issues for 'Giver.giver_url'
        raise RuntimeError("Cannot reverse this migration. 'Giver.giver_url' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Giver.giver_url'
        db.alter_column(u'giver_app_giver', 'giver_url', self.gf('django.db.models.fields.CharField')(max_length=1000))

        # User chose to not deal with backwards NULL issues for 'Giver.image'
        raise RuntimeError("Cannot reverse this migration. 'Giver.image' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Giver.image'
        db.alter_column(u'giver_app_giver', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

        # User chose to not deal with backwards NULL issues for 'Giver.description'
        raise RuntimeError("Cannot reverse this migration. 'Giver.description' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Giver.description'
        db.alter_column(u'giver_app_giver', 'description', self.gf('django.db.models.fields.CharField')(max_length=2000))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'charity_app.charity': {
            'Meta': {'object_name': 'Charity'},
            'charity_url': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'cover_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '6000', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'slogan': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'charity'", 'to': u"orm['auth.User']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'giver_app.giver': {
            'Meta': {'object_name': 'Giver'},
            'charities': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'givers'", 'symmetrical': 'False', 'to': u"orm['charity_app.Charity']"}),
            'cover_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True'}),
            'giver_url': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'slogan': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'giver'", 'to': u"orm['auth.User']"}),
            'video_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'})
        }
    }

    complete_apps = ['giver_app']