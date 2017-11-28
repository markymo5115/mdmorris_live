from django.db.models.query import QuerySet
from django.conf import settings

class SharedQueries(object):

	"""Some queries that are identical for Gallery and Photo."""

	def is_public(self):
		"""Trivial filter - but with added ordering"""
		return self.filter(is_public=True)


	def on_site(self):
		"""Returns objects linked to the current site only."""
		return self.filter(sites__id=settings.SITE_ID)

class GalleryQuerySet(SharedQueries, QuerySet):
	pass

class PhotoQuerySet(SharedQueries, QuerySet):
	pass
