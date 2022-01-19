from django.core import paginator
from django.shortcuts import render
from servicios.models import servicio
from django.core.paginator import Paginator
# Create your views here.


def servicios(request):
    #Le indicamos que importe todos los servicios que hayamos construido en la clase servicio
    listado_servicios=servicio.objects.all()
    paginator=Paginator(listado_servicios, 2)
    pagina=request.GET.get("page") or 1
    posts=paginator.get_page(pagina)
    pagina_actual=int(pagina)
    paginas=range(1, posts.paginator.num_pages + 1)
   #Le decimos a la plantilla que los muestre
    return render(request,"servicios/servicios.html", {"posts":posts, "paginas":paginas, "pagina_actual":pagina_actual})