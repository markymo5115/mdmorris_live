from django import forms
from django.contrib import admin

from ckeditor.widgets import CKEditorWidget
from photologue.admin import GalleryAdmin as GalleryAdminDefault
from photologue.models import Gallery
from .models import GalleryExtended

class GalleryExtendedInline(admin.StackedInline):
	model = GalleryExtended
	can_delete = False

class GalleryAdminForm(forms.ModelForm):
	"""Replace the default description field, with one that uses a custom widget."""

	description = forms.CharField(widget=CKEditorWidget())

	class Meta:
		model = Gallery
		exclude = ['']

class GalleryAdmin(GalleryAdminDefault):
	form = GalleryAdminForm

	# Define our new one-to-one model as an inline of Photologue's Gallery model
	inlines = [GalleryExtendedInline, ]

admin.site.unregister(Gallery)
admin.site.register(Gallery, GalleryAdmin)
