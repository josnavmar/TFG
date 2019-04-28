"""LearnIA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from . import views

from text.views import *
from image.views import *

from image.views import image_index
from django.views.generic import RedirectView
from django.conf.urls.static import static

urlpatterns = [
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
    path('admin/', admin.site.urls),
    url(r'^welcome/$', views.index, name='index'),
    url(r'^image/$', image_index, name='image_index'),
    url(r'^text/$', text_index, name='index_text'),
    url(r'^text/graph/$', graficos, name='graficos'),
    url(r'^text/demo/$', demo_texto, name='demostracion_texto'),
    url(r'^image/graph/$', graficos_imagen, name='graficos_imagen'),
    url(r'^image/upload/$', image_upload, name='image_upload')
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
