from django.db import models
from django.utils.translation import ugettext_lazy as _

from south.db import db

from articles.models import *


class Migration:
    
    def forwards(self):
        
        # Adding field 'Article.subtitle'
        db.add_column('articles_article', 'subtitle', models.CharField(_("Sub Title"), max_length=255, blank=True, default=""))
        
    
    def backwards(self):
        
        # Deleting field 'Article.subtitle'
        db.delete_column('articles_article', 'subtitle')
        
