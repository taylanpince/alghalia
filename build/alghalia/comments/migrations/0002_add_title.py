from django.db import models
from django.utils.translation import ugettext_lazy as _

from south.db import db

from comments.models import *


class Migration:
    
    def forwards(self):
        
        # Adding field 'Comment.title'
        db.add_column('comments_comment', 'title', models.CharField(_("Title"), max_length=255, blank=True, default=""))
        
    
    def backwards(self):
        
        # Deleting field 'Comment.title'
        db.delete_column('comments_comment', 'title')
        
