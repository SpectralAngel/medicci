# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Administracion'
        db.create_table('hospital_administracion', (
            ('hospital', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['contactos.Hospital'], unique=True, primary_key=True)),
            ('propietario', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('administrador', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('jefe_de_compras', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('socios', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('hospital', ['Administracion'])

        # Adding model 'Quirofano'
        db.create_table('hospital_quirofano', (
            ('hospital', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['contactos.Hospital'], unique=True, primary_key=True)),
            ('posee_quirofano', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('jefe', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('instrumentista', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('secretaria', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('doctores', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('numero_de_quirofanos', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('numero_de_salas_de_parto', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('quirofanos_endoscopicos', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal('hospital', ['Quirofano'])

        # Adding model 'CentroDeImagenes'
        db.create_table('hospital_centrodeimagenes', (
            ('hospital', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['contactos.Hospital'], unique=True, primary_key=True)),
            ('cantidad_de_equipos', self.gf('django.db.models.fields.IntegerField')()),
            ('posee_tomografo', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('marca_tomografo', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('piensa_aquirir_tomografo', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('posee_resonancia_magnetica', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('piensa_aquirir_resonancia', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('posee_fluoroscopio', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('tipo_fluoroscopio', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('piensa_aquirir_fluoroscopio', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('posee_densitometro', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('tipo_densitometro', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('piensa_aquirir_densitometro', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('posee_mamografo', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('tipo_mamografo', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('piensa_aquirir_mamografo', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('posee_ultrasonido', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('cantidad_ultrasonidos', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('algun_ultrasonido_4D', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('piensa_aquirir_ultrasonido', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal('hospital', ['CentroDeImagenes'])

        # Adding model 'CentroTecnico'
        db.create_table('hospital_centrotecnico', (
            ('hospital', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['contactos.Hospital'], unique=True, primary_key=True)),
            ('jefe', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('tecnicos', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('radiologos', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('secretaria', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal('hospital', ['CentroTecnico'])

        # Adding model 'Hospitalizacion'
        db.create_table('hospital_hospitalizacion', (
            ('hospital', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['contactos.Hospital'], unique=True, primary_key=True)),
            ('posee_hospitalizacion', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('cuantas_habitaciones_posee', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('cuantas_habitaciones_dobles_posee', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('cuantas_habitaciones_sencillas_posee', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal('hospital', ['Hospitalizacion'])


    def backwards(self, orm):
        # Deleting model 'Administracion'
        db.delete_table('hospital_administracion')

        # Deleting model 'Quirofano'
        db.delete_table('hospital_quirofano')

        # Deleting model 'CentroDeImagenes'
        db.delete_table('hospital_centrodeimagenes')

        # Deleting model 'CentroTecnico'
        db.delete_table('hospital_centrotecnico')

        # Deleting model 'Hospitalizacion'
        db.delete_table('hospital_hospitalizacion')


    models = {
        'contactos.hospital': {
            'Meta': {'object_name': 'Hospital'},
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'zona': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hospitales'", 'to': "orm['contactos.Zona']"})
        },
        'contactos.zona': {
            'Meta': {'object_name': 'Zona'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'hospital.administracion': {
            'Meta': {'object_name': 'Administracion'},
            'administrador': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'hospital': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['contactos.Hospital']", 'unique': 'True', 'primary_key': 'True'}),
            'jefe_de_compras': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'propietario': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'socios': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'hospital.centrodeimagenes': {
            'Meta': {'object_name': 'CentroDeImagenes'},
            'algun_ultrasonido_4D': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'cantidad_de_equipos': ('django.db.models.fields.IntegerField', [], {}),
            'cantidad_ultrasonidos': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'hospital': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['contactos.Hospital']", 'unique': 'True', 'primary_key': 'True'}),
            'marca_tomografo': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'piensa_aquirir_densitometro': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'piensa_aquirir_fluoroscopio': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'piensa_aquirir_mamografo': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'piensa_aquirir_resonancia': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'piensa_aquirir_tomografo': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'piensa_aquirir_ultrasonido': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'posee_densitometro': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'posee_fluoroscopio': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'posee_mamografo': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'posee_resonancia_magnetica': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'posee_tomografo': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'posee_ultrasonido': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'tipo_densitometro': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'tipo_fluoroscopio': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'tipo_mamografo': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'})
        },
        'hospital.centrotecnico': {
            'Meta': {'object_name': 'CentroTecnico'},
            'hospital': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['contactos.Hospital']", 'unique': 'True', 'primary_key': 'True'}),
            'jefe': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'radiologos': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'secretaria': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'tecnicos': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'hospital.hospitalizacion': {
            'Meta': {'object_name': 'Hospitalizacion'},
            'cuantas_habitaciones_dobles_posee': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'cuantas_habitaciones_posee': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'cuantas_habitaciones_sencillas_posee': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'hospital': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['contactos.Hospital']", 'unique': 'True', 'primary_key': 'True'}),
            'posee_hospitalizacion': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        'hospital.quirofano': {
            'Meta': {'object_name': 'Quirofano'},
            'doctores': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'hospital': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['contactos.Hospital']", 'unique': 'True', 'primary_key': 'True'}),
            'instrumentista': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'jefe': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'numero_de_quirofanos': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'numero_de_salas_de_parto': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'posee_quirofano': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'quirofanos_endoscopicos': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'secretaria': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        }
    }

    complete_apps = ['hospital']