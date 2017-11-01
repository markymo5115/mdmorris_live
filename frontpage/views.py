from django.shortcuts import render

from .models import Introduction

def home_view(request):
	intro = Introduction.objects.filter(title='Home')[0]
	return render(request, 'frontpage/home.html', {'intro': intro})

def aboutme_view(request):
	intro = Introduction.objects.filter(title='About Me')[0]
	return render(request, 'frontpage/aboutme.html', {'intro': intro})

def contactme_view(request):
	intro = Introduction.objects.filter(title='Contact Me')[0]
	return render(request, 'frontpage/contactme.html', {'intro': intro})

def links_view(request, slug):
	intro = Introduction.objects.filter(slug=slug)[0]
	return render(request, 'frontpage/contactme.html', {'intro':intro})
