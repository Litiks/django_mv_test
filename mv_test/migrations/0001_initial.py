# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Group'
        db.create_table(u'mv_test_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
        ))
        db.send_create_signal(u'mv_test', ['Group'])

        # Adding model 'Variation'
        db.create_table(u'mv_test_variation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(related_name='variations', to=orm['mv_test.Group'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
            ('js_code', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal(u'mv_test', ['Variation'])

        # Adding model 'MVProfile'
        db.create_table(u'mv_test_mvprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='mv_profile', unique=True, null=True, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'mv_test', ['MVProfile'])

        # Adding M2M table for field variations on 'MVProfile'
        m2m_table_name = db.shorten_name(u'mv_test_mvprofile_variations')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mvprofile', models.ForeignKey(orm[u'mv_test.mvprofile'], null=False)),
            ('variation', models.ForeignKey(orm[u'mv_test.variation'], null=False))
        ))
        db.create_unique(m2m_table_name, ['mvprofile_id', 'variation_id'])

        # Adding model 'Goal'
        db.create_table(u'mv_test_goal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'mv_test', ['Goal'])

        # Adding model 'PageViewLog'
        db.create_table(u'mv_test_pageviewlog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(related_name='page_view_logs', to=orm['mv_test.MVProfile'])),
            ('url', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'mv_test', ['PageViewLog'])


    def backwards(self, orm):
        # Deleting model 'Group'
        db.delete_table(u'mv_test_group')

        # Deleting model 'Variation'
        db.delete_table(u'mv_test_variation')

        # Deleting model 'MVProfile'
        db.delete_table(u'mv_test_mvprofile')

        # Removing M2M table for field variations on 'MVProfile'
        db.delete_table(db.shorten_name(u'mv_test_mvprofile_variations'))

        # Deleting model 'Goal'
        db.delete_table(u'mv_test_goal')

        # Deleting model 'PageViewLog'
        db.delete_table(u'mv_test_pageviewlog')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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
        u'mv_test.pageviewlog': {
            'Meta': {'object_name': 'PageViewLog'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'page_view_logs'", 'to': u"orm['mv_test.MVProfile']"}),
            'url': ('django.db.models.fields.TextField', [], {})
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