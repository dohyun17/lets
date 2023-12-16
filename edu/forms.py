from .models import Feed
from django import forms

class FeedForm(forms.ModelForm):
    class Meta:
        model = Feed
        fields = ('content', 'photo')