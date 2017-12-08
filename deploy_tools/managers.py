from django.db.models.query import QuerySet
from django.conf import settings


class SharedQueries(object):

    """Some queries that are identical for Gallery and Photo."""

    def is_public(self):
        """Trivial filter - will probably become more complex as time goes by!"""
        return self.filter(is_public=True)

    def on_site(self):
        """Return objects linked to the current site only."""
        return self.filter(sites__id=settings.SITE_ID)


class GalleryQuerySet(SharedQueries, QuerySet):
#    def on_site(self):
#        return SharedQueries.on_site(self).order_by('date_added')
#
#    def is_public(self):
#        return SharedQueries.is_public(self).order_by('date_added')
     pass


class PhotoQuerySet(SharedQueries, QuerySet):
    def on_site(self):
        return SharedQueries.on_site(self).order_by('date_added')

    def is_public(self):
        return SharedQueries.is_public(self).order_by('date_added')

