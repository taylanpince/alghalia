from django.db import models
from django.utils.translation import ugettext_lazy as _

from south.db import db

from articles.models import *


class Migration:
    
    def forwards(self):
        
        # Mock model
        User = db.mock_model(model_name='User', db_table='auth_user', db_tablespace='', pk_field_name='id', pk_field_type=models.AutoField, pk_field_args=[], pk_field_kwargs={})
        
        # Adding field 'Article.author'
        db.add_column('articles_article', 'author', models.ForeignKey(User, related_name=_("Author"), blank=True, null=True))
        
    
    def backwards(self):
        
        # Deleting field 'Article.author'
        db.delete_column('articles_article', 'author_id')
        
