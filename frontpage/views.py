from django.shortcuts import render

from .models import Introduction

def home_view(request):
	intro = Introduction.objects.filter(slug='home-3').first()
	return render(request, 'frontpage/home.html', {'intro': intro})

def aboutme_view(request):
	intro = Introduction.objects.filter(slug='about-me').first()
	return render(request, 'frontpage/aboutme.html', {'intro': intro})

def contactme_view(request):
	intro = Introduction.objects.filter(slug='contact-me').first()
	return render(request, 'frontpage/contactme.html', {'intro': intro})

def links_view(request, slug):
	if slug == 'enamelling':
		intro = Introduction.objects.filter(slug='enamelling').first()
	else:
		intro = Introduction.objects.filter(slug='miniature-paintings').first()
	
	return render(request, 'frontpage/contactme.html', {'intro':intro})
