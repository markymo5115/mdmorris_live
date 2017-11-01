from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from .models import Introduction

class IntroductionAdminForm(forms.ModelForm):

	text = forms.CharField(widget=CKEditorWidget())
	image_description = forms.CharField(widget=CKEditorWidget(), required=False)

	class Meta:
		model = Introduction
		exclude = ['']

class IntroductionAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	form = IntroductionAdminForm





admin.site.register(Introduction, IntroductionAdmin)

