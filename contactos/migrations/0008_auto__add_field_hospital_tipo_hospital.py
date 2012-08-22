# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Hospital.tipo_hospital'
        db.add_column('contactos_hospital', 'tipo_hospital',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=2, blank=True),
                      keep_default=False)

        # Removing M2M table for field cuentas on 'Contacto'
        db.delete_table('contactos_contacto_cuentas')

        # Adding M2M table for field hospitales on 'Contacto'
        db.create_table('contactos_contacto_hospitales', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contacto', models.ForeignKey(orm['contactos.contacto'], null=False)),
            ('hospital', models.ForeignKey(orm['contactos.hospital'], null=False))
        ))
        db.create_unique('contactos_contacto_hospitales', ['contacto_id', 'hospital_id'])


    def backwards(self, orm):
        # Deleting field 'Hospital.tipo_hospital'
        db.delete_column('contactos_hospital', 'tipo_hospital')

        # Adding M2M table for field cuentas on 'Contacto'
        db.create_table('contactos_contacto_cuentas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contacto', models.ForeignKey(orm['contactos.contacto'], null=False)),
            ('cuenta', models.ForeignKey(orm['contactos.cuenta'], null=False))
        ))
        db.create_unique('contactos_contacto_cuentas', ['contacto_id', 'cuenta_id'])

        # Removing M2M table for field hospitales on 'Contacto'
        db.delete_table('contactos_contacto_hospitales')


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
        'contactos.ciclo': {
            'Meta': {'object_name': 'Ciclo'},
            'fin': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inicio': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'contactos.cita': {
            'Meta': {'object_name': 'Cita'},
            'contacto': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'citas'", 'to': "orm['contactos.Contacto']"}),
            'fecha_y_hora': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'motivo': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'publicada': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'citas'", 'null': 'True', 'to': "orm['auth.User']"}),
            'visitada': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        'contactos.clinica': {
            'Meta': {'object_name': 'Clinica'},
            'contacto': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'clinicas'", 'to': "orm['contactos.Contacto']"}),
            'direccion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
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
        'contactos.cuenta': {
            'Meta': {'object_name': 'Cuenta'},
            'hospital': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cuentas'", 'to': "orm['contactos.Hospital']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'contactos.departamento': {
            'Meta': {'object_name': 'Departamento'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'contactos.direccion': {
            'Meta': {'object_name': 'Direccion'},
            'calle': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ciudad': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'direcciones'", 'to': "orm['contactos.Municipio']"}),
            'contacto': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'direcciones'", 'to': "orm['contactos.Contacto']"}),
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'direcciones'", 'to': "orm['contactos.Departamento']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'contactos.email': {
            'Meta': {'object_name': 'Email'},
            'contacto': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'emails'", 'to': "orm['contactos.Contacto']"}),
            'correo': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'})
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
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'tipo_hospital': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'zona': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hospitales'", 'to': "orm['contactos.Zona']"})
        },
        'contactos.material': {
            'Meta': {'object_name': 'Material'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'contactos.materialutilizado': {
            'Meta': {'object_name': 'MaterialUtilizado'},
            'costo': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'utlizado'", 'to': "orm['contactos.Material']"}),
            'visita': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'materiales'", 'to': "orm['contactos.Visita']"})
        },
        'contactos.municipio': {
            'Meta': {'object_name': 'Municipio'},
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'municipios'", 'to': "orm['contactos.Departamento']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'contactos.producto': {
            'Meta': {'object_name': 'Producto'},
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marca': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'contactos.profile': {
            'Meta': {'object_name': 'Profile'},
            'configurado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'}),
            'zona': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'perfiles'", 'null': 'True', 'to': "orm['contactos.Zona']"})
        },
        'contactos.telefono': {
            'Meta': {'object_name': 'Telefono'},
            'contacto': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'telefonos'", 'to': "orm['contactos.Contacto']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'})
        },
        'contactos.venta': {
            'Meta': {'object_name': 'Venta'},
            'cuenta': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ventas'", 'to': "orm['contactos.Cuenta']"}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ventas'", 'to': "orm['contactos.Producto']"}),
            'vendedor': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'ventas'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'contactos.visita': {
            'Meta': {'object_name': 'Visita'},
            'comentarios': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'contacto': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'visitas'", 'to': "orm['contactos.Contacto']"}),
            'fecha_y_hora': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'productos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'visitas'", 'blank': 'True', 'to': "orm['contactos.Producto']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'visitas'", 'null': 'True', 'to': "orm['auth.User']"})
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
        }
    }

    complete_apps = ['contactos']