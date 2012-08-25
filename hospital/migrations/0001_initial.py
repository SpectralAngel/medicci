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
            ('propietario', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='propietario', null=True, to=orm['contactos.Contacto'])),
            ('administrador', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='administrador', null=True, to=orm['contactos.Contacto'])),
            ('jefe_de_compras', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='jefe_de_compras', null=True, to=orm['contactos.Contacto'])),
        ))
        db.send_create_signal('hospital', ['Administracion'])

        # Adding M2M table for field socios on 'Administracion'
        db.create_table('hospital_administracion_socios', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('administracion', models.ForeignKey(orm['hospital.administracion'], null=False)),
            ('contacto', models.ForeignKey(orm['contactos.contacto'], null=False))
        ))
        db.create_unique('hospital_administracion_socios', ['administracion_id', 'contacto_id'])

        # Adding model 'Quirofano'
        db.create_table('hospital_quirofano', (
            ('hospital', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['contactos.Hospital'], unique=True, primary_key=True)),
            ('posee_quirofano', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('jefe', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='jefe_quirofanos', null=True, to=orm['contactos.Contacto'])),
            ('instrumentista', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='instrumentista', null=True, to=orm['contactos.Contacto'])),
            ('secretaria', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='secretaria_quirofano', null=True, to=orm['contactos.Contacto'])),
            ('numero_de_quirofanos', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('numero_de_salas_de_parto', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('quirofanos_endoscopicos', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal('hospital', ['Quirofano'])

        # Adding M2M table for field doctores on 'Quirofano'
        db.create_table('hospital_quirofano_doctores', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('quirofano', models.ForeignKey(orm['hospital.quirofano'], null=False)),
            ('contacto', models.ForeignKey(orm['contactos.contacto'], null=False))
        ))
        db.create_unique('hospital_quirofano_doctores', ['quirofano_id', 'contacto_id'])

        # Adding model 'CentroDeImagenes'
        db.create_table('hospital_centrodeimagenes', (
            ('hospital', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['contactos.Hospital'], unique=True, primary_key=True)),
            ('cantidad_de_equipos', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
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
            ('jefe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contactos.Contacto'], null=True, blank=True)),
            ('secretaria', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='secretaria_tecnico', null=True, to=orm['contactos.Contacto'])),
        ))
        db.send_create_signal('hospital', ['CentroTecnico'])

        # Adding M2M table for field tecnicos on 'CentroTecnico'
        db.create_table('hospital_centrotecnico_tecnicos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('centrotecnico', models.ForeignKey(orm['hospital.centrotecnico'], null=False)),
            ('contacto', models.ForeignKey(orm['contactos.contacto'], null=False))
        ))
        db.create_unique('hospital_centrotecnico_tecnicos', ['centrotecnico_id', 'contacto_id'])

        # Adding M2M table for field radiologos on 'CentroTecnico'
        db.create_table('hospital_centrotecnico_radiologos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('centrotecnico', models.ForeignKey(orm['hospital.centrotecnico'], null=False)),
            ('contacto', models.ForeignKey(orm['contactos.contacto'], null=False))
        ))
        db.create_unique('hospital_centrotecnico_radiologos', ['centrotecnico_id', 'contacto_id'])

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

        # Removing M2M table for field socios on 'Administracion'
        db.delete_table('hospital_administracion_socios')

        # Deleting model 'Quirofano'
        db.delete_table('hospital_quirofano')

        # Removing M2M table for field doctores on 'Quirofano'
        db.delete_table('hospital_quirofano_doctores')

        # Deleting model 'CentroDeImagenes'
        db.delete_table('hospital_centrodeimagenes')

        # Deleting model 'CentroTecnico'
        db.delete_table('hospital_centrotecnico')

        # Removing M2M table for field tecnicos on 'CentroTecnico'
        db.delete_table('hospital_centrotecnico_tecnicos')

        # Removing M2M table for field radiologos on 'CentroTecnico'
        db.delete_table('hospital_centrotecnico_radiologos')

        # Deleting model 'Hospitalizacion'
        db.delete_table('hospital_hospitalizacion')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contactos.asociacion': {
            'Meta': {'object_name': 'Asociacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'contactos.contacto': {
            'Meta': {'object_name': 'Contacto'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'agregado': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'asociaciones': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'contactos'", 'symmetrical': 'False', 'to': "orm['contactos.Asociacion']"}),
            'ciudad': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contactos'", 'blank': 'True', 'to': "orm['contactos.Municipio']"}),
            'especialidades': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'contactos'", 'blank': 'True', 'to': "orm['contactos.Especialidad']"}),
            'horario': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'hospitales': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'contactos'", 'blank': 'True', 'to': "orm['contactos.Hospital']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nacimiento': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'vendedores': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'contactos'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'web': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'contactos.departamento': {
            'Meta': {'object_name': 'Departamento'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'contactos.especialidad': {
            'Meta': {'object_name': 'Especialidad'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'contactos.hospital': {
            'Meta': {'object_name': 'Hospital'},
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hospitales'", 'to': "orm['contactos.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'tipo_hospital': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'zona': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hospitales'", 'to': "orm['contactos.Zona']"})
        },
        'contactos.municipio': {
            'Meta': {'object_name': 'Municipio'},
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'municipios'", 'to': "orm['contactos.Departamento']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'contactos.zona': {
            'Meta': {'object_name': 'Zona'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'hospital.administracion': {
            'Meta': {'object_name': 'Administracion'},
            'administrador': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'administrador'", 'null': 'True', 'to': "orm['contactos.Contacto']"}),
            'hospital': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['contactos.Hospital']", 'unique': 'True', 'primary_key': 'True'}),
            'jefe_de_compras': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'jefe_de_compras'", 'null': 'True', 'to': "orm['contactos.Contacto']"}),
            'propietario': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'propietario'", 'null': 'True', 'to': "orm['contactos.Contacto']"}),
            'socios': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['contactos.Contacto']", 'symmetrical': 'False'})
        },
        'hospital.centrodeimagenes': {
            'Meta': {'object_name': 'CentroDeImagenes'},
            'algun_ultrasonido_4D': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'cantidad_de_equipos': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
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
            'jefe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contactos.Contacto']", 'null': 'True', 'blank': 'True'}),
            'radiologos': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'radiologs'", 'symmetrical': 'False', 'to': "orm['contactos.Contacto']"}),
            'secretaria': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'secretaria_tecnico'", 'null': 'True', 'to': "orm['contactos.Contacto']"}),
            'tecnicos': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'tecnicos'", 'symmetrical': 'False', 'to': "orm['contactos.Contacto']"})
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
            'doctores': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'doctores'", 'symmetrical': 'False', 'to': "orm['contactos.Contacto']"}),
            'hospital': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['contactos.Hospital']", 'unique': 'True', 'primary_key': 'True'}),
            'instrumentista': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'instrumentista'", 'null': 'True', 'to': "orm['contactos.Contacto']"}),
            'jefe': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'jefe_quirofanos'", 'null': 'True', 'to': "orm['contactos.Contacto']"}),
            'numero_de_quirofanos': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'numero_de_salas_de_parto': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'posee_quirofano': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'quirofanos_endoscopicos': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'secretaria': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'secretaria_quirofano'", 'null': 'True', 'to': "orm['contactos.Contacto']"})
        }
    }

    complete_apps = ['hospital']