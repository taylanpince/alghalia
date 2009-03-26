from django.db import models
from django.contrib.contenttypes.models import ContentType


class CommentManager(models.Manager):
    """
    Returns only published comments
    """
    def get_query_set(self):
        return super(CommentManager, self).get_query_set().filter(published=True)

    def get_for_model(self, model):
        """
        QuerySet for all comments for a particular model (either an instance or a class)
        """
        content_type = ContentType.objects.get_for_model(model)

        qs = self.get_query_set().filter(content_type=content_type)

        if isinstance(model, models.Model):
            qs = qs.filter(object_id=model.id)

        return qs
