# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Show.imageurl'
        db.add_column('cms_show', 'imageurl',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Show.imageurl'
        db.delete_column('cms_show', 'imageurl')

    models = {
        'cms.grouping': {
            'Meta': {'object_name': 'Grouping'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'cms.page': {
            'Meta': {'object_name': 'Page'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'frontpage': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'unique': 'True'}),
            'grouping': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Grouping']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'cms.show': {
            'Meta': {'object_name': 'Show'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'dj': ('django.db.models.fields.CharField', [], {'max_length': '420'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'imageurl': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'songfile': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'songfile_length': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'songfile_size': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'year': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['cms']