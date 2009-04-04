from django.db import models
from django.utils.translation import ugettext_lazy as _

from south.db import db

from articles.models import *


class Migration:
    
    def forwards(self):
        
        # Mock model
        ArticleCategory = db.mock_model(model_name='ArticleCategory', db_table='articles_articlecategory', db_tablespace='', pk_field_name='id', pk_field_type=models.AutoField, pk_field_args=[], pk_field_kwargs={})
        
        # Adding field 'ArticleCategory.parent'
        db.add_column('articles_articlecategory', 'parent', models.ForeignKey(ArticleCategory, verbose_name=_("Parent Category"), limit_choices_to={ "parent__isnull": True, }, blank=True, null=True, related_name="sub_categories"))
        
    
    def backwards(self):
        
        # Deleting field 'ArticleCategory.parent'
        db.delete_column('articles_articlecategory', 'parent_id')
        
