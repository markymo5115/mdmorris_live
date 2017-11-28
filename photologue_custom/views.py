from django.shortcuts import render
from photologue.views import PhotoListView, GalleryDetailView
from django.views.generic.detail import DetailView
#from braces.views import JSONResponseMixin

from .models import MyGallery
#from photologue.models import Gallery

#class PhotoJSONListView(JSONResponseMixin, PhotoListView):

#	def render_to_response(self, context, **response_kwargs):
#		return self.render_json_object_response(context['object_list'], **response_kwargs)

class MyGalleryDetailView(DetailView):
   queryset = MyGallery.objects.on_site().is_public()
   
   #lets use photologues generic views, need to tell django to use gallery and 
   #not mygallery as the object name in the template, also need to tell it to
   #use photologues template!

   context_object_name = 'gallery'
   template_name = 'photologue/gallery_detail.html'




