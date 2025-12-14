from django.shortcuts import render

from app1.models import Usuario
from app3.models import Articulo
from app6.models import Comentario
from app7.models import Favorito
from app8.models import Biblioteca
from app5.models import Revision
from app9.models import Etiqueta

def dashboard_view(request):
    # Obtenemos los datos de cada modelo
    context = {
        "usuarios": Usuario.objects.count(),
        "articulos": Articulo.objects.count(),
        "comentarios": Comentario.objects.count(),
        "favoritos": Favorito.objects.count(),
        "biblioteca": Biblioteca.objects.count(),
        "revisiones": Revision.objects.count(),
        "etiquetas": Etiqueta.objects.count(),
    }
    
    # Puedes añadir más detalles si lo deseas, como las últimas entradas
    context["ultimos_articulos"] = Articulo.objects.all().order_by('-fecha_creacion')[:5]
    context["ultimos_comentarios"] = Comentario.objects.all().order_by('-fecha_creacion')[:5]
    
    return render(request, "dashboard/index.html", context)
