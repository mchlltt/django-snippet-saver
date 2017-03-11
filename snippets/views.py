from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView

from .forms import SnippetForm
from .models import Snippet


class SnippetList(ListView):
    model = Snippet
    context_object_name = 'snippets'


def home(request):
    if request.method == 'GET':
        form = SnippetForm()

    else:
        # Bind data from request.POST into a PostForm
        form = SnippetForm(request.POST)

        # If data is valid, proceeds to create a new snippet and redirect the user to snippets.
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('snippets/')

    context = {
        'form': form
    }

    return render(request, 'snippets/home.html', context)
