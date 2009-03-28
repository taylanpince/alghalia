from django.contrib.contenttypes.models import ContentType


def with_comment_count(qs):
    """
    Extends `qs` to include a `comment_count` column
    """
    content_type = ContentType.objects.get_for_model(qs.model)

    return qs.extra(
        select={
            'comment_count':
            """
            SELECT count(*) FROM comments_comment
            WHERE content_type_id=%(content_type_id)s 
            AND object_id=%(object_id)s.id
            """ % {
                'content_type_id': content_type.id, 
                'object_id': qs.model._meta.db_table,
            }
        }
    )
