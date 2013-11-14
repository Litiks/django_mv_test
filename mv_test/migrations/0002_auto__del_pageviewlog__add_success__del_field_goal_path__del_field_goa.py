# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'PageViewLog'
        db.delete_table(u'mv_test_pageviewlog')

        # Adding model 'Success'
        db.create_table(u'mv_test_success', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(related_name='successes', to=orm['mv_test.MVProfile'])),
            ('goal', self.gf('django.db.models.fields.related.ForeignKey')(related_name='successes', to=orm['mv_test.Goal'])),
        ))
        db.send_create_signal(u'mv_test', ['Success'])

        # Deleting field 'Goal.path'
        db.delete_column(u'mv_test_goal', 'path')

        # Deleting field 'Goal.name'
        db.delete_column(u'mv_test_goal', 'name')

        # Adding field 'Goal.slug'
        db.add_column(u'mv_test_goal', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'PageViewLog'
        db.create_table(u'mv_test_pageviewlog', (
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(related_name='page_view_logs', to=orm['mv_test.MVProfile'])),
            ('url', self.gf('django.db.models.fields.TextField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'mv_test', ['PageViewLog'])

        # Deleting model 'Success'
        db.delete_table(u'mv_test_success')


        # User chose to not deal with backwards NULL issues for 'Goal.path'
        raise RuntimeError("Cannot reverse this migration. 'Goal.path' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Goal.path'
        db.add_column(u'mv_test_goal', 'path',
                      self.gf('django.db.models.fields.CharField')(max_length=200),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Goal.name'
        raise RuntimeError("Cannot reverse this migration. 'Goal.name' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Goal.name'
        db.add_column(u'mv_test_goal', 'name',
                      self.gf('django.db.models.fields.CharField')(max_length=100),
                      keep_default=False)

        # Deleting field 'Goal.slug'
        db.delete_column(u'mv_test_goal', 'slug')


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'mv_test.goal': {
            'Meta': {'object_name': 'Goal'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        },
        u'mv_test.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        },
        u'mv_test.mvprofile': {
            'Meta': {'object_name': 'MVProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'mv_profile'", 'unique': 'True', 'null': 'True', 'to': u"orm['auth.User']"}),
            'variations': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'profiles'", 'symmetrical': 'False', 'to': u"orm['mv_test.Variation']"})
        },
        u'mv_test.success': {
            'Meta': {'object_name': 'Success'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'goal': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'successes'", 'to': u"orm['mv_test.Goal']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'successes'", 'to': u"orm['mv_test.MVProfile']"})
        },
        u'mv_test.variation': {
            'Meta': {'object_name': 'Variation'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'variations'", 'to': u"orm['mv_test.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'js_code': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['mv_test']