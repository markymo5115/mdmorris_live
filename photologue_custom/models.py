from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.urlresolvers import reverse

from sortedm2m.fields import SortedManyToManyField

from taggit.managers import TaggableManager

from photologue.models import Gallery, Photo

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


def map_to_proxy(instance, proxy_class):
   new_instance = proxy_class()
 
   for field in instance._meta.fields:
      value = getattr(instance, field.name)
      setattr(new_instance, field.name, value)

   return new_instance
	
	
class MyGallery(Gallery):

   class Meta:
      proxy = True


   def public(self):
      """Return a queryset of all the public photos in this gallery. And put them in reverse order, ie. earliest date taken first."""
      temp = self.photos.is_public().filter(sites__id=settings.SITE_ID).order_by('date_added')
      temp2 = [map_to_proxy(temp[i], MyPhoto) for i in range(0, len(temp))] 
      return temp2
      

   def get_absolute_url(self):
      return reverse('photologue-custom:pl-projects', args=[self.slug])


class MyPhoto(Photo):
    """Created this proxy model so that the ordering is chronologically increasing. A simpler method would be to change photologues own manager methods but then is would be difficult to keep the urls for projects sepparate"""
    class Meta:
        proxy = True
        ordering = ['date_added']

    def get_previous_in_gallery(self, gallery):
        """Find the neighbour of this photo in the supplied gallery.
        We assume that the gallery and all its photos are on the same site.
        """
        if not self.is_public:
            raise ValueError('Cannot determine neighbours of a non-public photo.')
        photos = gallery.photos.is_public().order_by('date_added')
        photos = [map_to_proxy(photos[i], MyPhoto) for i in range(0, len(photos))] 
        if self not in photos:
            raise ValueError('Photo does not belong to gallery.')
        previous = None
        for photo in photos:
            if photo == self:
                return previous
            previous = photo

    def get_next_in_gallery(self, gallery):
        """Find the neighbour of this photo in the supplied gallery.
        We assume that the gallery and all its photos are on the same site.
        """
        if not self.is_public:
            raise ValueError('Cannot determine neighbours of a non-public photo.')
        photos = gallery.photos.is_public().order_by('date_added')
        photos = [map_to_proxy(photos[i], MyPhoto) for i in range(0, len(photos))] 
        if self not in photos:
            raise ValueError('Photo does not belong to gallery.')
        matched = False
        for photo in photos:
            if matched:
                return photo
            if photo == self:
                matched = True
        return None

    def public_galleries(self):
        """Return the public galleries to which this photo belongs."""
        temp = self.galleries.filter(is_public=True)
#        for i in range(0,len(temp)):
#           if temp[i].isProjectGallery:
#              temp[i]=map_to_proxy(temp[i],MyGallery)
        temp = [map_to_proxy(temp[i], MyGallery) for i in range(0, len(temp))]
        return temp
	

    def get_absolute_url(self):
       return reverse('photologue-custom:pl-projects-photo', args=[self.slug])
