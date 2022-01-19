from django.urls import path, include
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name="Home"),

]
#Registramos la url para que sea de busqueda de multimedia y podamos visualizar lo que haya en la raiz
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


