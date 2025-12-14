from django.core.mail import EmailMessage


def enviar_pdf_por_correo(destino, archivo, password):
    email = EmailMessage(
        subject="Reporte confidencial de actividad",
        body=f"""
Hola,

Adjunto encontrarás tu reporte personal en PDF.

🔐 CONTRASEÑA DEL PDF:
{password}

Por seguridad, no compartas este archivo con terceros.

Saludos,
Sistema Académico
""",
        to=[destino]
    )

    email.attach_file(archivo)
    email.send()
