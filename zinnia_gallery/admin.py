from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from zinnia.models.entry import Entry
from zinnia.admin.entry import EntryAdmin

#from .models import Gallery, Picture

class EntryGalleryAdmin(EntryAdmin):
	# In our case we put the gallery filed 
	# into the 'Content' fieldset
	fieldsets = (
		(_('Content'), {
			'fields':(('title', 'status'), 'lead', 'content',)}),
		(_('Illustration'), {
			'fields': ('picture','image_caption', 'gallery'),
			'classes': ('collapse', 'collapse-closed',)}),) + \
		EntryAdmin.fieldsets[2:]

admin.site.register(Entry, EntryGalleryAdmin)
#admin.site.register(Gallery)
#admin.site.register(Picture)

