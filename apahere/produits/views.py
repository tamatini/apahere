from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Biens
from .forms import ProduitForm
from proprietaire.views import CreateOwner

# Create your views here.

def produits_page(request):
    context = {
        'produits': Biens.objects.all()
    }
    return render(request, 'produits/produits.html', context)


class CreateProduits(CreateView):
    model = Biens
    form_class = ProduitForm
    success_url = reverse_lazy('produits')
