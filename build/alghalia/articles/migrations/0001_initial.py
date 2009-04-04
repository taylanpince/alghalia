from django.db import models
from django.utils.translation import ugettext_lazy as _

from south.db import db

from articles.models import *


class Migration:
    
    def forwards(self):
        
        # Model 'ArticleCategory'
        db.create_table('articles_articlecategory', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('name', models.CharField(_("Name"), max_length=255)),
            ('slug', models.SlugField(_("Slug"), max_length=255, unique=True)),
            ('theme', models.CharField(_("Colour Theme"), max_length=10, choices=THEME_CHOICES)),
            ('featured', models.BooleanField(_("Featured"), default=False)),
        ))
        
        # Mock Models
        ArticleCategory = db.mock_model(model_name='ArticleCategory', db_table='articles_articlecategory', db_tablespace='', pk_field_name='id', pk_field_type=models.AutoField, pk_field_args=[], pk_field_kwargs={})
        
        # Model 'Article'
        db.create_table('articles_article', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('title', models.CharField(_("Title"), max_length=255)),
            ('slug', models.SlugField(_("Slug"), max_length=255)),
            ('summary', models.TextField(_("Summary"), blank=True)),
            ('body', models.TextField(_("Body"), blank=True)),
            ('category', models.ForeignKey(ArticleCategory, verbose_name=_("Category"))),
            ('tags', TagField(_("Tags"))),
            ('featured', models.BooleanField(_("Featured"), default=False)),
            ('published', models.BooleanField(_("Published"), default=True)),
            ('publication_date', models.DateTimeField(_("Publication Date"), default=datetime.now)),
            ('expiration_date', models.DateTimeField(_("Expiration Date"), blank=True, null=True)),
            ('creation_date', models.DateTimeField(_("Creation Date"), editable=False, auto_now_add=True)),
            ('modification_date', models.DateTimeField(_("Modification Date"), editable=False, auto_now=True)),
            ('view_count', models.PositiveIntegerField(_("View Count"), editable=False, default=0)),
        ))
        db.create_index('articles_article', ['slug','publication_date','category_id'], unique=True, db_tablespace='')
        
        
        db.send_create_signal('articles', ['ArticleCategory','Article'])
    
    def backwards(self):
        db.delete_table('articles_article')
        db.delete_table('articles_articlecategory')
        
