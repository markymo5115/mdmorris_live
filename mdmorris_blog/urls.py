"""mdmorris_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
#from django.contrib.sitemaps.views import index
from django.contrib.sitemaps.views import sitemap
from django.views.defaults import bad_request, page_not_found, permission_denied, server_error


from django.views.generic.base import RedirectView
from django_xmlrpc.views import handle_xmlrpc
from frontpage import views as frontpage_views

from zinnia.sitemaps import AuthorSitemap
from zinnia.sitemaps import CategorySitemap
from zinnia.sitemaps import EntrySitemap
from zinnia.sitemaps import TagSitemap
from photologue.sitemaps import GallerySitemap, PhotoSitemap
from django.views.generic import TemplateView

import photologue_custom

urlpatterns = [
   url(r'^home/$', frontpage_views.home_view, name='home'),
   url(r'^about-me/$', frontpage_views.aboutme_view, name='about_me'),
#   url(r'^how-to-order', RedirectView.as_view(url='home', permanent=True), name='commission'),
   url(r'^contact-mark/$', frontpage_views.contactme_view, name='contact-me'),
   url(r'^links/(?P<slug>[\-\d\w]+)/$', frontpage_views.links_view, name='links'),
#   url(r'^buy-a-necklace', RedirectView.as_view(url='home', permanent=True), name='buy-a-necklace'),
#  url(r'^view-cart', RedirectView.as_view(url='home', permanent=True), name='view-cart'),
#  url(r'^blog', RedirectView.as_view(url='photologue/', permanent=True), name='blog'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^weblog/sitemap/', RedirectView.as_view(url='/sitemap.xml', permanent=True), name='sitemap'),
    url(r'^weblog/', include('zinnia.urls', namespace='zinnia')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^xmlrpc/$', handle_xmlrpc),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^projects/', include('photologue_custom.urls', namespace='photologue-custom')),
    url(r'^explore/', include('photologue.urls', namespace='photologue')),
    url(r'^$', RedirectView.as_view(url='home', permanent=True))
] 


sitemaps = {
	'tags': TagSitemap,
	'blog':EntrySitemap,
	'authors': AuthorSitemap,
	'categories': CategorySitemap,
	'photologue_galleries': GallerySitemap,
	'photologue_photos': PhotoSitemap,
}

urlpatterns += [
#************************
# This doesn't work so replaced using sitemap instead of index, worked!
#	url(r'^sitemap.xml$',
#		index,
#		{'sitemaps': sitemaps}),
#******************************
	url(r'^sitemap.xml$',
		sitemap,
		{'sitemaps': sitemaps}),
	
	url(r'^sitemap-(?P<section>.+)\.xml$',
		sitemap,
		{'sitemaps': sitemaps}, name='sitemaps'),
	]

urlpatterns += [
	url(r'^400/$', bad_request),
	url(r'^403/$', permission_denied),
	url(r'^404/$', page_not_found),
	url(r'^500/$', server_error),
]

#Add Bing Verify Ownership Authentication and Google verification too
urlpatterns += [
	url(r'^BingSiteAuth\.xml', TemplateView.as_view(template_name='zinnia/BingSiteAuth.xml', content_type='text/xml')),
	url(r'^googled9943244a1802ac7\.html', TemplateView.as_view(template_name='zinnia/googled9943244a1802ac7.html', content_type='text/html')),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, 
		document_root=settings.MEDIA_ROOT)
