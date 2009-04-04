from django.db import models
from django.utils.translation import ugettext_lazy as _

from south.db import db

from comments.models import *


class Migration:
    
    def forwards(self):
        
        
        # Mock Models
        ContentType = db.mock_model(model_name='ContentType', db_table='django_content_type', db_tablespace='', pk_field_name='id', pk_field_type=models.AutoField, pk_field_args=[], pk_field_kwargs={})
        
        # Model 'Comment'
        db.create_table('comments_comment', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('body', models.TextField(_("Comment"))),
            ('published', models.BooleanField(_("Published"), default=True)),
            ('author', models.CharField(_("Name"), blank=True, max_length=255)),
            ('email', models.EmailField(_("Email"), blank=True)),
            ('ip_address', models.IPAddressField(_("IP Address"), blank=True, null=True)),
            ('content_type', models.ForeignKey(ContentType)),
            ('object_id', models.PositiveIntegerField()),
            ('creation_date', models.DateTimeField(_("Creation Date"), editable=False, auto_now_add=True)),
            ('modification_date', models.DateTimeField(_("Modification Date"), editable=False, auto_now=True)),
        ))
        
        db.send_create_signal('comments', ['Comment'])
    
    def backwards(self):
        db.delete_table('comments_comment')
        
