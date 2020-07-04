from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.blog_page, name='blog'),
    url(r'^new_post$', views.new_post_page, name="new_post")
]