from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django import forms

from ckeditor.widgets import CKEditorWidget
from zinnia.models.entry import Entry

from zinnia.admin.entry import EntryAdmin

#from .models import Gallery, Picture
class EntryGalleryAdminForm(forms.ModelForm):
	"""Replace the default content field with one that uses a custom widget."""
	lead = forms.CharField(widget=CKEditorWidget())
	content = forms.CharField(widget=CKEditorWidget())

	class Meta:
		model = Entry
		exclude = ['']

class EntryGalleryAdmin(EntryAdmin):
	# In our case we put the gallery field 
	# into the 'Content' fieldset

	form = EntryGalleryAdminForm

	fieldsets = (
		(_('Content'), {
			'fields':(('title', 'status'), 'lead', 'content',)}),
		(_('Illustration'), {
			'fields': ('picture','image_caption', 'gallery'),
			'classes': ('collapse', 'collapse-closed',)}),) + \
		EntryAdmin.fieldsets[2:]


admin.site.register(Entry, EntryGalleryAdmin)

