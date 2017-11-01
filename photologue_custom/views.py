from django.shortcuts import render
from photologue.views import PhotoListView, GalleryDetailView
from django.views.generic.detail import DetailView
from braces.views import JSONResponseMixin

from .models import GalleryExtended, MyGallery

class PhotoJSONListView(JSONResponseMixin, PhotoListView):

	def render_to_response(self, context, **response_kwargs):
		return self.render_json_object_response(context['object_list'], **response_kwargs)

class MyGalleryDetailView(DetailView):
	queryset = MyGallery.objects.on_site().is_public()
	template_name = 'mygallery_detail.html'
	pass

