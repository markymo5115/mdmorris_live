from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.urlresolvers import reverse

#from sortedm2m.fields import SortedManyToManyField

from taggit.managers import TaggableManager

from photologue.models import Gallery, Photo
from photologue.managers import GalleryQuerySet, PhotoQuerySet

class GalleryExtended(models.Model):

	# Link back to Photologue's Gallery model.
	gallery = models.OneToOneField(Gallery, related_name='extended')

	# This is the important bit - where we add in the tags.
	tags = TaggableManager(blank=True)

	# Boilderplate code to make a prettier display in the admin interface.
	class Meta:
	   verbose_name = u'Extra fields'
	   verbose_name_plural = u'Extra fields'

	def __str__(self):
	   return self.gallery.title

	def get_absolute_url(self):
  	   return reverse('gallery', args=[self.gallery.slug])

class MyGallery(Gallery):

   class Meta:
      proxy = True

   def public(self):
      """Return a queryset of all the public photos in this gallery. And put them in reverse order, ie. earliest date taken first."""
      temp = self.photos.is_public().filter(sites__id=settings.SITE_ID)
      return temp.order_by('date_added')

#	def get_absolute_url(self):
#	   return reverse('photologue-custom:pl-projects', args=[self.slug])

#class MyPhoto(Photo):
#	
#	class Meta:
#		proxy = True
#		ordering = ['date_added']
#
