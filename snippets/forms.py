from django.forms import ModelForm

from . import models


class SnippetForm(ModelForm):
    class Meta:
        model = models.Snippet
        fields = '__all__'