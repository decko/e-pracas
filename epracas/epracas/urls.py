"""epracas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from atividades.views import CriarAtividade, ModificarAtividade, ListarAtividade, ExcluirAtividade

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'atividade/add/$', CriarAtividade.as_view(), name='atividade-add'),
    url(r'atividade/(?P<pk>[0-9]+)/$', ModificarAtividade.as_view(), name='atividade-update'),
    url(r'^$', ListarAtividade.as_view(), name='atividade-list'),
    url(r'^atividade/excluir/(?P<pk>[0-9]+)/$', ExcluirAtividade.as_view(), name='atividade-delete'),
    url(r'^chaining/', include('smart_selects.urls')),
]
