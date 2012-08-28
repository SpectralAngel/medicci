# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ResonanciaMagenetica'
        db.create_table('hospital_resonanciamagenetica', (
            ('centro_de_imagenes', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['hospital.CentroDeImagenes'], unique=True, primary_key=True)),
            ('posee_resonancia_magnetica', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('piensa_aquirir_resonancia', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal('hospital', ['ResonanciaMagenetica'])

        # Adding model 'Fluoroscopia'
        db.create_table('hospital_fluoroscopia', (
            ('centro_de_imagenes', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['hospital.CentroDeImagenes'], unique=True, primary_key=True)),
            ('posee_fluoroscopio', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('tipo_fluoroscopio', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('piensa_aquirir_fluoroscopio', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal('hospital', ['Fluoroscopia'])

        # Adding model 'Mamografia'
        db.create_table('hospital_mamografia', (
            ('centro_de_imagenes', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['hospital.CentroDeImagenes'], unique=True, primary_key=True)),
            ('posee_mamografo', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('tipo_mamografo', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('piensa_aquirir_mamografo', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal('hospital', ['Mamografia'])

        # Adding model 'Ecografia'
        db.create_table('hospital_ecografia', (
            ('centro_de_imagenes', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['hospital.CentroDeImagenes'], unique=True, primary_key=True)),
            ('posee_ultrasonido', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('cantidad_ultrasonidos', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('algun_ultrasonido_4D', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('piensa_aquirir_ultrasonido', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal('hospital', ['Ecografia'])

        # Adding model 'Tomografia'
        db.create_table('hospital_tomografia', (
            ('centro_de_imagenes', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['hospital.CentroDeImagenes'], unique=True, primary_key=True)),
            ('posee_tomografo', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('marca_tomografo', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('piensa_aquirir_tomografo', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal('hospital', ['Tomografia'])

        # Adding model 'Densitometria'
        db.create_table('hospital_densitometria', (
            ('centro_de_imagenes', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['hospital.CentroDeImagenes'], unique=True, primary_key=True)),
            ('posee_densitometro', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('tipo_densitometro', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('piensa_aquirir_densitometro', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal('hospital', ['Densitometria'])

        # Deleting field 'CentroDeImagenes.piensa_aquirir_mamografo'
        db.delete_column('hospital_centrodeimagenes', 'piensa_aquirir_mamografo')

        # Deleting field 'CentroDeImagenes.piensa_aquirir_fluoroscopio'
        db.delete_column('hospital_centrodeimagenes', 'piensa_aquirir_fluoroscopio')

        # Deleting field 'CentroDeImagenes.piensa_aquirir_ultrasonido'
        db.delete_column('hospital_centrodeimagenes', 'piensa_aquirir_ultrasonido')

        # Deleting field 'CentroDeImagenes.piensa_aquirir_resonancia'
        db.delete_column('hospital_centrodeimagenes', 'piensa_aquirir_resonancia')

        # Deleting field 'CentroDeImagenes.posee_densitometro'
        db.delete_column('hospital_centrodeimagenes', 'posee_densitometro')

        # Deleting field 'CentroDeImagenes.posee_resonancia_magnetica'
        db.delete_column('hospital_centrodeimagenes', 'posee_resonancia_magnetica')

        # Deleting field 'CentroDeImagenes.tipo_mamografo'
        db.delete_column('hospital_centrodeimagenes', 'tipo_mamografo')

        # Deleting field 'CentroDeImagenes.posee_mamografo'
        db.delete_column('hospital_centrodeimagenes', 'posee_mamografo')

        # Deleting field 'CentroDeImagenes.piensa_aquirir_tomografo'
        db.delete_column('hospital_centrodeimagenes', 'piensa_aquirir_tomografo')

        # Deleting field 'CentroDeImagenes.posee_fluoroscopio'
        db.delete_column('hospital_centrodeimagenes', 'posee_fluoroscopio')

        # Deleting field 'CentroDeImagenes.tipo_fluoroscopio'
        db.delete_column('hospital_centrodeimagenes', 'tipo_fluoroscopio')

        # Deleting field 'CentroDeImagenes.posee_tomografo'
        db.delete_column('hospital_centrodeimagenes', 'posee_tomografo')

        # Deleting field 'CentroDeImagenes.piensa_aquirir_densitometro'
        db.delete_column('hospital_centrodeimagenes', 'piensa_aquirir_densitometro')

        # Deleting field 'CentroDeImagenes.algun_ultrasonido_4D'
        db.delete_column('hospital_centrodeimagenes', 'algun_ultrasonido_4D')

        # Deleting field 'CentroDeImagenes.tipo_densitometro'
        db.delete_column('hospital_centrodeimagenes', 'tipo_densitometro')

        # Deleting field 'CentroDeImagenes.posee_ultrasonido'
        db.delete_column('hospital_centrodeimagenes', 'posee_ultrasonido')

        # Deleting field 'CentroDeImagenes.marca_tomografo'
        db.delete_column('hospital_centrodeimagenes', 'marca_tomografo')

        # Deleting field 'CentroDeImagenes.cantidad_ultrasonidos'
        db.delete_column('hospital_centrodeimagenes', 'cantidad_ultrasonidos')


    def backwards(self, orm):
        # Deleting model 'ResonanciaMagenetica'
        db.delete_table('hospital_resonanciamagenetica')

        # Deleting model 'Fluoroscopia'
        db.delete_table('hospital_fluoroscopia')

        # Deleting model 'Mamografia'
        db.delete_table('hospital_mamografia')

        # Deleting model 'Ecografia'
        db.delete_table('hospital_ecografia')

        # Deleting model 'Tomografia'
        db.delete_table('hospital_tomografia')

        # Deleting model 'Densitometria'
        db.delete_table('hospital_densitometria')

        # Adding field 'CentroDeImagenes.piensa_aquirir_mamografo'
        db.add_column('hospital_centrodeimagenes', 'piensa_aquirir_mamografo',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'CentroDeImagenes.piensa_aquirir_fluoroscopio'
        db.add_column('hospital_centrodeimagenes', 'piensa_aquirir_fluoroscopio',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'CentroDeImagenes.piensa_aquirir_ultrasonido'
        db.add_column('hospital_centrodeimagenes', 'piensa_aquirir_ultrasonido',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'CentroDeImagenes.piensa_aquirir_resonancia'
        db.add_column('hospital_centrodeimagenes', 'piensa_aquirir_resonancia',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'CentroDeImagenes.posee_densitometro'
        db.add_column('hospital_centrodeimagenes', 'posee_densitometro',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'CentroDeImagenes.posee_resonancia_magnetica'
        db.add_column('hospital_centrodeimagenes', 'posee_resonancia_magnetica',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'CentroDeImagenes.tipo_mamografo'
        db.add_column('hospital_centrodeimagenes', 'tipo_mamografo',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1, blank=True),
                      keep_default=False)

        # Adding field 'CentroDeImagenes.posee_mamografo'
        db.add_column('hospital_centrodeimagenes', 'posee_mamografo',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'CentroDeImagenes.piensa_aquirir_tomografo'
        db.add_column('hospital_centrodeimagenes', 'piensa_aquirir_tomografo',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'CentroDeImagenes.posee_fluoroscopio'
        db.add_column('hospital_centrodeimagenes', 'posee_fluoroscopio',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'CentroDeImagenes.tipo_fluoroscopio'
        db.add_column('hospital_centrodeimagenes', 'tipo_fluoroscopio',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1, blank=True),
                      keep_default=False)

        # Adding field 'CentroDeImagenes.posee_tomografo'
        db.add_column('hospital_centrodeimagenes', 'posee_tomografo',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'CentroDeImagenes.piensa_aquirir_densitometro'
        db.add_column('hospital_centrodeimagenes', 'piensa_aquirir_densitometro',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'CentroDeImagenes.algun_ultrasonido_4D'
        db.add_column('hospital_centrodeimagenes', 'algun_ultrasonido_4D',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'CentroDeImagenes.tipo_densitometro'
        db.add_column('hospital_centrodeimagenes', 'tipo_densitometro',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1, blank=True),
                      keep_default=False)

        # Adding field 'CentroDeImagenes.posee_ultrasonido'
        db.add_column('hospital_centrodeimagenes', 'posee_ultrasonido',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'CentroDeImagenes.marca_tomografo'
        db.add_column('hospital_centrodeimagenes', 'marca_tomografo',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'CentroDeImagenes.cantidad_ultrasonidos'
        db.add_column('hospital_centrodeimagenes', 'cantidad_ultrasonidos',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)


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
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'asociaciones': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'contactos'", 'symmetrical': 'False', 'to': "orm['contactos.Asociacion']"}),
            'ciudad': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contactos'", 'blank': 'True', 'to': "orm['contactos.Municipio']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            'especialidades': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'contactos'", 'blank': 'True', 'to': "orm['contactos.Especialidad']"}),
            'horario': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'hospitales': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'contactos'", 'symmetrical': 'False', 'to': "orm['contactos.Hospital']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nacimiento': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'telefono': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
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
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hospitales'", 'to': "orm['contactos.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tipo_hospital': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
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
            'cantidad_de_equipos': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'hospital': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['contactos.Hospital']", 'unique': 'True', 'primary_key': 'True'}),
            'jefe': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'jefe_imagenes'", 'null': 'True', 'to': "orm['contactos.Contacto']"}),
            'radiologos': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'radiologos'", 'symmetrical': 'False', 'to': "orm['contactos.Contacto']"}),
            'secretaria': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'secretaria_imagenes'", 'null': 'True', 'to': "orm['contactos.Contacto']"}),
            'tecnicos': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'tecnicos'", 'symmetrical': 'False', 'to': "orm['contactos.Contacto']"})
        },
        'hospital.densitometria': {
            'Meta': {'object_name': 'Densitometria'},
            'centro_de_imagenes': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['hospital.CentroDeImagenes']", 'unique': 'True', 'primary_key': 'True'}),
            'piensa_aquirir_densitometro': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'posee_densitometro': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'tipo_densitometro': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'})
        },
        'hospital.ecografia': {
            'Meta': {'object_name': 'Ecografia'},
            'algun_ultrasonido_4D': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'cantidad_ultrasonidos': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'centro_de_imagenes': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['hospital.CentroDeImagenes']", 'unique': 'True', 'primary_key': 'True'}),
            'piensa_aquirir_ultrasonido': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'posee_ultrasonido': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        'hospital.fluoroscopia': {
            'Meta': {'object_name': 'Fluoroscopia'},
            'centro_de_imagenes': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['hospital.CentroDeImagenes']", 'unique': 'True', 'primary_key': 'True'}),
            'piensa_aquirir_fluoroscopio': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'posee_fluoroscopio': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'tipo_fluoroscopio': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'})
        },
        'hospital.hospitalizacion': {
            'Meta': {'object_name': 'Hospitalizacion'},
            'cuantas_habitaciones_dobles_posee': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'cuantas_habitaciones_posee': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'cuantas_habitaciones_sencillas_posee': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'cuantas_habitaciones_suite_posee': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'director_medico': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'director_medico'", 'null': 'True', 'to': "orm['contactos.Contacto']"}),
            'hospital': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['contactos.Hospital']", 'unique': 'True', 'primary_key': 'True'}),
            'hospitalizador': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'hospitalizador'", 'null': 'True', 'to': "orm['contactos.Contacto']"}),
            'posee_hospitalizacion': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        'hospital.mamografia': {
            'Meta': {'object_name': 'Mamografia'},
            'centro_de_imagenes': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['hospital.CentroDeImagenes']", 'unique': 'True', 'primary_key': 'True'}),
            'piensa_aquirir_mamografo': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'posee_mamografo': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'tipo_mamografo': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'})
        },
        'hospital.quirofano': {
            'Meta': {'object_name': 'Quirofano'},
            'anestesiologos': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'anestesiologos'", 'symmetrical': 'False', 'to': "orm['contactos.Contacto']"}),
            'cirujanos': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'cirujanos'", 'symmetrical': 'False', 'to': "orm['contactos.Contacto']"}),
            'hospital': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['contactos.Hospital']", 'unique': 'True', 'primary_key': 'True'}),
            'instrumentistas': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'instrumentistas'", 'symmetrical': 'False', 'to': "orm['contactos.Contacto']"}),
            'jefe': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'jefe_quirofanos'", 'null': 'True', 'to': "orm['contactos.Contacto']"}),
            'licenciado': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'licenciado_quirofanos'", 'null': 'True', 'to': "orm['contactos.Contacto']"}),
            'numero_de_quirofanos': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'numero_de_salas_de_parto': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'posee_quirofano': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'quirofanos_endoscopicos': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'secretaria': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'secretaria_quirofano'", 'null': 'True', 'to': "orm['contactos.Contacto']"})
        },
        'hospital.resonanciamagenetica': {
            'Meta': {'object_name': 'ResonanciaMagenetica'},
            'centro_de_imagenes': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['hospital.CentroDeImagenes']", 'unique': 'True', 'primary_key': 'True'}),
            'piensa_aquirir_resonancia': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'posee_resonancia_magnetica': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        'hospital.tomografia': {
            'Meta': {'object_name': 'Tomografia'},
            'centro_de_imagenes': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['hospital.CentroDeImagenes']", 'unique': 'True', 'primary_key': 'True'}),
            'marca_tomografo': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'piensa_aquirir_tomografo': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'posee_tomografo': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['hospital']