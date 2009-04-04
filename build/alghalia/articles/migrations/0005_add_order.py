from django.db import models
from django.utils.translation import ugettext_lazy as _

from south.db import db

from articles.models import *


class Migration:
    
    def forwards(self):
        
        # Adding field 'ArticleCategory.order'
        db.add_column('articles_articlecategory', 'order', models.PositiveSmallIntegerField(_("Order"), default=0))
        
    
    def backwards(self):
        
        # Deleting field 'ArticleCategory.order'
        db.delete_column('articles_articlecategory', 'order')
        
