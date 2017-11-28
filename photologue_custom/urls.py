from django.conf.urls import url
from .views import MyGalleryDetailView, MyPhotoDetailView

urlpatterns = [
	url(r'^gallery/(?P<slug>[\-\d\w]+)/$',
		MyGalleryDetailView.as_view(),
		name='pl-projects'),
	url(r'^photo/(?P<slug>[\-\d\w]+)/$',
		MyPhotoDetailView.as_view(),
		name='pl-projects-photo'),
	
]
