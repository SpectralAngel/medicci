# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ciclo'
        db.create_table('contactos_ciclo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('inicio', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('fin', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
        ))
        db.send_create_signal('contactos', ['Ciclo'])

        # Adding model 'Departamento'
        db.create_table('contactos_departamento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal('contactos', ['Departamento'])

        # Adding model 'Municipio'
        db.create_table('contactos_municipio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('departamento', self.gf('django.db.models.fields.related.ForeignKey')(related_name='municipios', to=orm['contactos.Departamento'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal('contactos', ['Municipio'])

        # Adding model 'Especialidad'
        db.create_table('contactos_especialidad', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('contactos', ['Especialidad'])

        # Adding model 'Cuenta'
        db.create_table('contactos_cuenta', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
        ))
        db.send_create_signal('contactos', ['Cuenta'])

        # Adding model 'Contacto'
        db.create_table('contactos_contacto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('sexo', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('nacimiento', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('web', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('ciudad', self.gf('django.db.models.fields.related.ForeignKey')(related_name='contactos', blank=True, to=orm['contactos.Municipio'])),
        ))
        db.send_create_signal('contactos', ['Contacto'])

        # Adding M2M table for field especialidades on 'Contacto'
        db.create_table('contactos_contacto_especialidades', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contacto', models.ForeignKey(orm['contactos.contacto'], null=False)),
            ('especialidad', models.ForeignKey(orm['contactos.especialidad'], null=False))
        ))
        db.create_unique('contactos_contacto_especialidades', ['contacto_id', 'especialidad_id'])

        # Adding M2M table for field cuentas on 'Contacto'
        db.create_table('contactos_contacto_cuentas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contacto', models.ForeignKey(orm['contactos.contacto'], null=False)),
            ('cuenta', models.ForeignKey(orm['contactos.cuenta'], null=False))
        ))
        db.create_unique('contactos_contacto_cuentas', ['contacto_id', 'cuenta_id'])

        # Adding M2M table for field vendedores on 'Contacto'
        db.create_table('contactos_contacto_vendedores', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contacto', models.ForeignKey(orm['contactos.contacto'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('contactos_contacto_vendedores', ['contacto_id', 'user_id'])

        # Adding model 'Direccion'
        db.create_table('contactos_direccion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contacto', self.gf('django.db.models.fields.related.ForeignKey')(related_name='direcciones', to=orm['contactos.Contacto'])),
            ('calle', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('ciudad', self.gf('django.db.models.fields.related.ForeignKey')(related_name='direcciones', to=orm['contactos.Municipio'])),
            ('departamento', self.gf('django.db.models.fields.related.ForeignKey')(related_name='direcciones', to=orm['contactos.Departamento'])),
        ))
        db.send_create_signal('contactos', ['Direccion'])

        # Adding model 'Telefono'
        db.create_table('contactos_telefono', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contacto', self.gf('django.db.models.fields.related.ForeignKey')(related_name='telefonos', to=orm['contactos.Contacto'])),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('numero', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('contactos', ['Telefono'])

        # Adding model 'Email'
        db.create_table('contactos_email', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contacto', self.gf('django.db.models.fields.related.ForeignKey')(related_name='emails', to=orm['contactos.Contacto'])),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('correo', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('contactos', ['Email'])

        # Adding model 'Horario'
        db.create_table('contactos_horario', (
            ('contacto', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['contactos.Contacto'], unique=True, primary_key=True)),
            ('dias_de_semana', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('fin_de_semana', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
        ))
        db.send_create_signal('contactos', ['Horario'])

        # Adding model 'Producto'
        db.create_table('contactos_producto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('marca', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('contactos', ['Producto'])

        # Adding model 'Material'
        db.create_table('contactos_material', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('contactos', ['Material'])

        # Adding model 'Cita'
        db.create_table('contactos_cita', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contacto', self.gf('django.db.models.fields.related.ForeignKey')(related_name='citas', to=orm['contactos.Contacto'])),
            ('fecha_y_hora', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('visitada', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='citas', null=True, to=orm['auth.User'])),
            ('motivo', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('contactos', ['Cita'])

        # Adding model 'Visita'
        db.create_table('contactos_visita', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contacto', self.gf('django.db.models.fields.related.ForeignKey')(related_name='visitas', to=orm['contactos.Contacto'])),
            ('fecha_y_hora', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('comentarios', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='visitas', null=True, to=orm['auth.User'])),
        ))
        db.send_create_signal('contactos', ['Visita'])

        # Adding M2M table for field productos on 'Visita'
        db.create_table('contactos_visita_productos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('visita', models.ForeignKey(orm['contactos.visita'], null=False)),
            ('producto', models.ForeignKey(orm['contactos.producto'], null=False))
        ))
        db.create_unique('contactos_visita_productos', ['visita_id', 'producto_id'])

        # Adding model 'MaterialUtilizado'
        db.create_table('contactos_materialutilizado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('visita', self.gf('django.db.models.fields.related.ForeignKey')(related_name='materiales', to=orm['contactos.Visita'])),
            ('material', self.gf('django.db.models.fields.related.ForeignKey')(related_name='utlizado', to=orm['contactos.Material'])),
            ('costo', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2)),
        ))
        db.send_create_signal('contactos', ['MaterialUtilizado'])


    def backwards(self, orm):
        # Deleting model 'Ciclo'
        db.delete_table('contactos_ciclo')

        # Deleting model 'Departamento'
        db.delete_table('contactos_departamento')

        # Deleting model 'Municipio'
        db.delete_table('contactos_municipio')

        # Deleting model 'Especialidad'
        db.delete_table('contactos_especialidad')

        # Deleting model 'Cuenta'
        db.delete_table('contactos_cuenta')

        # Deleting model 'Contacto'
        db.delete_table('contactos_contacto')

        # Removing M2M table for field especialidades on 'Contacto'
        db.delete_table('contactos_contacto_especialidades')

        # Removing M2M table for field cuentas on 'Contacto'
        db.delete_table('contactos_contacto_cuentas')

        # Removing M2M table for field vendedores on 'Contacto'
        db.delete_table('contactos_contacto_vendedores')

        # Deleting model 'Direccion'
        db.delete_table('contactos_direccion')

        # Deleting model 'Telefono'
        db.delete_table('contactos_telefono')

        # Deleting model 'Email'
        db.delete_table('contactos_email')

        # Deleting model 'Horario'
        db.delete_table('contactos_horario')

        # Deleting model 'Producto'
        db.delete_table('contactos_producto')

        # Deleting model 'Material'
        db.delete_table('contactos_material')

        # Deleting model 'Cita'
        db.delete_table('contactos_cita')

        # Deleting model 'Visita'
        db.delete_table('contactos_visita')

        # Removing M2M table for field productos on 'Visita'
        db.delete_table('contactos_visita_productos')

        # Deleting model 'MaterialUtilizado'
        db.delete_table('contactos_materialutilizado')


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
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'citas'", 'null': 'True', 'to': "orm['auth.User']"}),
            'visitada': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        'contactos.contacto': {
            'Meta': {'object_name': 'Contacto'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'ciudad': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contactos'", 'blank': 'True', 'to': "orm['contactos.Municipio']"}),
            'cuentas': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'contactos'", 'blank': 'True', 'to': "orm['contactos.Cuenta']"}),
            'especialidades': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'contactos'", 'blank': 'True', 'to': "orm['contactos.Especialidad']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nacimiento': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'vendedores': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'contactos'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'web': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'contactos.cuenta': {
            'Meta': {'object_name': 'Cuenta'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'})
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
        'contactos.horario': {
            'Meta': {'object_name': 'Horario'},
            'contacto': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['contactos.Contacto']", 'unique': 'True', 'primary_key': 'True'}),
            'dias_de_semana': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'fin_de_semana': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'})
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
        'contactos.telefono': {
            'Meta': {'object_name': 'Telefono'},
            'contacto': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'telefonos'", 'to': "orm['contactos.Contacto']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'})
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
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['contactos']