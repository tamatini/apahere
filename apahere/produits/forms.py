from django import forms
from .models import Biens, Photo_biens
from proprietaire.models import Proprietaire


class ProduitForm(forms.ModelForm):
    class Meta:
        model = Biens
        proprietaire = forms.ModelChoiceField(queryset=Proprietaire.objects.all())
        fields = '__all__'


class ImagesForm(forms.ModelForm):
    class Meta:
        model = Photo_biens
        fields = '__all__'