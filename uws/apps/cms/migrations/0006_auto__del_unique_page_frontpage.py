# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Page', fields ['frontpage']
        db.delete_unique('cms_page', ['frontpage'])

    def backwards(self, orm):
        # Adding unique constraint on 'Page', fields ['frontpage']
        db.create_unique('cms_page', ['frontpage'])

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
            'frontpage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'songfile_length': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'songfile_size': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True'}),
            'year': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['cms']