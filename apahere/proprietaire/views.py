from django.shortcuts import render
from .models import Proprietaire
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView


# Create your views here.
def owner_page(request):
    context = {
        'owners': Proprietaire.objects.all()
    }
    return render(request, 'proprietaire/owner.html', context)


class ListOwner(ListView):
    model = Proprietaire
    template_name = 'proprietaire/owner.html'
    context_object_name = "owners"
    

class CreateOwner(CreateView):
    model = Proprietaire
    fields = [
        'nom',
        'prenom',
        'tel',
        'mail',
    ]


class DetailOwner(DetailView):
    model = Proprietaire


class UpdateOwner(UpdateView):
    model = Proprietaire
    fields = [
        'nom',
        'prenom',
        'tel',
        'mail',
    ]
    template_name_suffix = '_update_form'


class DeleteOwner(DeleteView):
    model = Proprietaire
    success_url = reverse_lazy('list-owner')