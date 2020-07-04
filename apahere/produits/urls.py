from django.conf.urls import url
from django.urls import path
from produits import views


urlpatterns = [
    url(r'^$', views.produits_page, name='produits'),
    path('new/', views.CreateProduits.as_view(), name='create-produit'),
] 