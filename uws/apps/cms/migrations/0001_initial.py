# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Show'
        db.create_table('cms_show', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dj', self.gf('django.db.models.fields.CharField')(max_length=420)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('songfile', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('year', self.gf('django.db.models.fields.PositiveIntegerField')(blank=True)),
            ('songfile_size', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('songfile_length', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('cms', ['Show'])

        # Adding model 'Grouping'
        db.create_table('cms_grouping', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('position', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('cms', ['Grouping'])

        # Adding model 'Page'
        db.create_table('cms_page', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('grouping', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Grouping'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal('cms', ['Page'])

    def backwards(self, orm):
        # Deleting model 'Show'
        db.delete_table('cms_show')

        # Deleting model 'Grouping'
        db.delete_table('cms_grouping')

        # Deleting model 'Page'
        db.delete_table('cms_page')

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
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'songfile': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'songfile_length': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'songfile_size': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'year': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['cms']