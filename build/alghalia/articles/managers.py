from datetime import datetime

from django.db import models


class ArticleManager(models.Manager):
    """
    A custom manager that takes into account the expiration, publication dates
    and the published flag
    """
    def get_query_set(self):
        return super(ArticleManager, self).get_query_set().filter(
            models.Q(publication_date__lte=datetime.now()) & (
                models.Q(expiration_date__isnull=True) | \
                models.Q(expiration_date__gt=datetime.now()) \
            ) & models.Q(published=True)
        )
