from django.shortcuts import render
from . import models
from django.http import HttpResponseRedirect
from . import forms

# Create your views here.
def home(request):
    if request.method == 'GET':
        form = forms.SnippetForm()
    else:
        # A POST request: Handle Form Upload
        # Bind data from request.POST into a PostForm
        form = forms.SnippetForm(request.POST)
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('snippets/')

    return render(request, 'snippets/home.html', {
        'form': form,
    })

def snippets(request):
    return render(request, 'snippets/snippets.html', {
        'snippets': models.Snippet.objects.all()
    })