from django.core.management.base import BaseCommand

from app1.models import Usuario
from app3.models import Articulo
from app6.models import Comentario
from app7.models import Favorito
from app8.models import Biblioteca
from app5.models import Revision

from app_reportes.pdf_utils import generar_pdf_usuario
from app_reportes.email_utils import enviar_pdf_por_correo


class Command(BaseCommand):
    help = "Envía un PDF con toda la actividad de un usuario"

    def handle(self, *args, **kwargs):

        print("\nUsuarios disponibles:\n")
        for u in Usuario.objects.all():
            print(f"{u.id_usuario} - {u.nombre}")

        user_id = input("\nIngrese ID del usuario: ")
        correo = input("Ingrese correo Gmail destino: ")

        usuario = Usuario.objects.get(id_usuario=user_id)

        # ===== CONSULTAS A TODAS LAS APIS =====
        articulos = Articulo.objects.filter(autor=usuario)
        comentarios = Comentario.objects.filter(usuario=usuario)
        favoritos = Favorito.objects.filter(usuario=usuario)
        biblioteca = Biblioteca.objects.filter(subido_por=usuario)
        revisiones = Revision.objects.filter(revisor__usuario=usuario)

        # 🔐 CONTRASEÑA MODIFICABLE
        password_pdf = usuario.email  # <- CAMBIA AQUÍ SI QUIERES

        archivo_pdf = generar_pdf_usuario(
            usuario,
            articulos,
            comentarios,
            favoritos,
            biblioteca,
            revisiones,
            password_pdf
        )

        enviar_pdf_por_correo(correo, archivo_pdf, password_pdf)

        self.stdout.write(
            self.style.SUCCESS("✅ PDF completo generado y enviado correctamente")
        )
