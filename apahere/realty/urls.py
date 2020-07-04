from django.conf.urls import url
from realty import views

urlpatterns = [
    url(r'^new_client$', views.new_client, name="new_client")
]
