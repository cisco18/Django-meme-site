from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm
from .models import Meme
from .humanize import naturalsize
from django.core.files.uploadedfile import InMemoryUploadedFile


class CreateMemeForm(forms.ModelForm):

    class Meta:
        model = Meme
        fields = ['title', 'picture']
