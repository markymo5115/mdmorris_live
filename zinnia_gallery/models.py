import os

from django.utils import timezone
from django.db import models
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify

from zinnia.models_bases import entry
from zinnia.settings import UPLOAD_TO
from zinnia.settings import AUTO_CLOSE_PINGBACKS_AFTER
from zinnia.settings import AUTO_CLOSE_TRACKBACKS_AFTER
from zinnia.settings import AUTO_CLOSE_COMMENTS_AFTER

from photologue.models import Gallery, Photo





#class Picture(models.Model):
#
#	def image_upload_to(self, filename):
#		"""
#		#Compute the upload pate for the image field.
#		"""
#
#		now = timezone.now()
#		filename, extension = os.path.splitext(filename)
#
#		return os.path.join(
#			UPLOAD_TO,
#			now.strftime('%Y'),
#			now.strftime('%m'),
#			now.strftime('%d'),
#			'%s%s' % (slugify(filename), extension))
#
#	title = models.CharField(_('title'), max_length=50)
#	image = models.ImageField(_('image'),
#				blank=True,
#				upload_to=entry.image_upload_to_dispatcher,
#			#	upload_to='gallery',
#				help_text=_('Used for illustration.'))
#
##	image_caption = models.TextField(
##				_('caption'),
##				blank=True,
##				help_text=_("Image's caption."))
#
#
#	def __str__(self):
#		return self.title
#
#class Gallery(models.Model):
#	title = models.CharField(_('title'),
#				max_length=50)
#	pictures = models.ManyToManyField(Picture)
#
#	class Meta:
#		verbose_name = "Gallery"
#		verbose_name_plural = "Galleries"
#		ordering = ['title']
#
#	def __str__(self):
#		return self.title


#redefine this to make default False for comments enabled
class DiscussionsEntry(models.Model):
    """
    Abstract discussion model class providing
    the fields and methods to manage the discussions
    (comments, pingbacks, trackbacks).
    """
    comment_enabled = models.BooleanField(
        _('comments enabled'), default=False,
        help_text=_('Allows comments if checked.'))
    pingback_enabled = models.BooleanField(
        _('pingbacks enabled'), default=True,
        help_text=_('Allows pingbacks if checked.'))
    trackback_enabled = models.BooleanField(
        _('trackbacks enabled'), default=True,
        help_text=_('Allows trackbacks if checked.'))

    comment_count = models.IntegerField(
        _('comment count'), default=0)
    pingback_count = models.IntegerField(
        _('pingback count'), default=0)
    trackback_count = models.IntegerField(
        _('trackback count'), default=0)

    @property
    def discussions(self):
        """
        Returns a queryset of the published discussions.
        """
        return comments.get_model().objects.for_model(
            self).filter(is_public=True, is_removed=False)

    @property
    def comments(self):
        """
        Returns a queryset of the published comments.
        """
        return self.discussions.filter(Q(flags=None) | Q(
            flags__flag=CommentFlag.MODERATOR_APPROVAL))

    @property
    def pingbacks(self):
        """
        Returns a queryset of the published pingbacks.
        """
        return self.discussions.filter(flags__flag=PINGBACK)

    @property
    def trackbacks(self):
        """
        Return a queryset of the published trackbacks.
        """
        return self.discussions.filter(flags__flag=TRACKBACK)

    def discussion_is_still_open(self, discussion_type, auto_close_after):
        """
        Checks if a type of discussion is still open
        are a certain number of days.
        """
        discussion_enabled = getattr(self, discussion_type)
        if (discussion_enabled and isinstance(auto_close_after, int) and
                auto_close_after >= 0):
            return (timezone.now() - (
                self.start_publication or self.publication_date)).days < \
                auto_close_after
        return discussion_enabled

    @property
    def comments_are_open(self):
        """
        Checks if the comments are open with the
        AUTO_CLOSE_COMMENTS_AFTER setting.
        """
        return self.discussion_is_still_open(
            'comment_enabled', AUTO_CLOSE_COMMENTS_AFTER)

    @property
    def pingbacks_are_open(self):
        """
        Checks if the pingbacks are open with the
        AUTO_CLOSE_PINGBACKS_AFTER setting.
        """
        return self.discussion_is_still_open(
            'pingback_enabled', AUTO_CLOSE_PINGBACKS_AFTER)

    @property
    def trackbacks_are_open(self):
        """
        Checks if the trackbacks are open with the
        AUTO_CLOSE_TRACKBACKS_AFTER setting.
        """
        return self.discussion_is_still_open(
            'trackback_enabled', AUTO_CLOSE_TRACKBACKS_AFTER)

    class Meta:
        abstract = True

#class EntryGallery(entry.AbstractEntry):
#	gallery = models.ForeignKey(Gallery)

#	def __str__(self):
#		return 'EntryGallery %s' %self.title

#	class Meta(entry.AbstractEntry.Meta):
#		abstract = True

		
class EntryGallery(
		entry.CoreEntry,
		entry.ContentEntry,
		DiscussionsEntry,
		entry.RelatedEntry,
		entry.LeadEntry,
		entry.ExcerptEntry,
		entry.FeaturedEntry,
		entry.AuthorsEntry,
		entry.CategoriesEntry,
		entry.TagsEntry,
		entry.LoginRequiredEntry,
		entry.PasswordRequiredEntry,
		entry.ContentTemplateEntry,
		entry.DetailTemplateEntry):

	#picture = models.ForeignKey(Picture,null=True, blank=True)
	picture = models.ForeignKey(Photo, null=True, blank=True)
	image_caption = models.CharField(_('caption'),
				max_length = 50,
				blank=True)

	#gallery = models.ForeignKey(Gallery,null=True, blank=True)
	gallery = models.ForeignKey(Gallery,null=True, blank=True)

	@property	
	def image(self):
		if not(self.picture==None):
			return self.picture.image
		else:
			return None

	def __str__(self):
		return 'EntryGallery %s' % self.title

	
	class Meta(entry.CoreEntry.Meta):
		abstract = True
