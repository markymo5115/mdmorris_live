from django.db import models
from django.utils.translation import ugettext_lazy as _
from photologue.models import Photo


class Introduction(models.Model):
	title = models.CharField(max_length=200, verbose_name='Title', unique=True)
	slug = models.CharField(max_length=200, 
				verbose_name='slug',
				default=title)
	text = models.TextField(verbose_name="Text")
	picture = models.ForeignKey(Photo, null=True, blank=True)
	image_caption = models.CharField(_('caption'),
				max_length = 50,
				blank=True,
				null=True)
	image_description = models.TextField(verbose_name="Image Text", null=True,blank=True)

	class Meta:
		verbose_name = "Introduction"

	def __str__(self):
		return self.title

	@property
	def image(self):
		if not(self.picture==None):
			return self.picture.image
		else:
			return None
