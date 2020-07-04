from django.conf.urls import url
from django.urls import path
from proprietaire import views


urlpatterns = [
    path('', views.ListOwner.as_view(), name='list-owner'),
    path('new/', views.CreateOwner.as_view(), name='create-owner'),
    path('<int:pk>/', views.DetailOwner.as_view(), name='detail-owner'),
    path('<int:pk>/update', views.UpdateOwner.as_view(), name='update-owner'),
    path('<int:pk>/delete', views.DeleteOwner.as_view(), name='delete-owner')
]