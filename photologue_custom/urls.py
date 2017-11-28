from django.conf.urls import url
from .views import MyGalleryDetailView

urlpatterns = [
	url(r'^gallery/(?P<slug>[\-\d\w]+)/$',
		MyGalleryDetailView.as_view(),
		name='pl-projects'),
]
