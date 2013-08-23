# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pesapal'
        db.create_table(u'core_pesapal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tracking_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('reference', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('status', self.gf('django.db.models.fields.CharField')(default='PENDING', max_length=9)),
        ))
        db.send_create_signal(u'core', ['Pesapal'])


    def backwards(self, orm):
        # Deleting model 'Pesapal'
        db.delete_table(u'core_pesapal')


    models = {
        u'core.pesapal': {
            'Meta': {'object_name': 'Pesapal'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'PENDING'", 'max_length': '9'}),
            'tracking_id': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['core']