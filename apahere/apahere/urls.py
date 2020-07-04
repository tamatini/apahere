"""apahere URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from realty import views as homepage_view
from realty import urls as realty_urls
from produits import urls as produits_urls
from services import views as services_view
from blog import urls as blog_urls
from agents import views as agents_view
from contact import views as contact_view
from proprietaire import urls as owner_urls
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', homepage_view.homepage, name="home"),
    path('admin/', admin.site.urls),
    url(r'^produits/', include(produits_urls)),
    url(r'^realty/', include(realty_urls)),
    url(r'^services/', services_view.services_page, name="services"),
    url(r'^blog/', include(blog_urls)),
    url(r'^agents/', agents_view.agents_page, name="agents"),
    url(r'^contact/', contact_view.contact_page, name="contact"),
    url(r'^owners/', include(owner_urls))
]+ static(settings.BIEN_URL, document_root=settings.BIENS_ROOT)
