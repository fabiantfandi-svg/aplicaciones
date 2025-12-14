from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
import os


def generar_pdf_usuario(
    usuario,
    articulos,
    comentarios,
    favoritos,
    biblioteca,
    revisiones,
    password
):
    temp = "reporte_usuario_temp.pdf"
    final = f"reporte_usuario_{usuario.id_usuario}.pdf"

    c = canvas.Canvas(temp, pagesize=letter)
    width, height = letter

    def titulo(texto, y):
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, y, texto)

    def texto(texto, y):
        c.setFont("Helvetica", 11)
        c.drawString(70, y, texto)

    y = height - 50

    # ===== DATOS DEL USUARIO =====
    titulo("REPORTE GENERAL DEL USUARIO", y)
    y -= 30

    texto(f"Nombre: {usuario.nombre}", y)
    y -= 20
    texto(f"Email: {usuario.email}", y)
    y -= 30

    # ===== ARTÍCULOS =====
    titulo("Artículos creados", y)
    y -= 20
    for art in articulos:
        texto(f"- {art.titulo}", y)
        y -= 15

    y -= 20

    # ===== COMENTARIOS =====
    titulo("Comentarios realizados", y)
    y -= 20
    for cmt in comentarios:
        texto(f"- {cmt.contenido[:60]}", y)
        y -= 15

    y -= 20

    # ===== FAVORITOS =====
    titulo("Artículos favoritos", y)
    y -= 20
    for fav in favoritos:
        texto(f"- {fav.articulo.titulo}", y)
        y -= 15

    y -= 20

    # ===== BIBLIOTECA =====
    titulo("Recursos subidos a biblioteca", y)
    y -= 20
    for b in biblioteca:
        texto(f"- {b.titulo}", y)
        y -= 15

    y -= 20

    # ===== REVISIONES =====
    titulo("Revisiones realizadas", y)
    y -= 20
    for r in revisiones:
        texto(f"- Artículo ID {r.articulo.id_articulo} → {r.recomendacion}", y)
        y -= 15

    c.save()

    # ===== ENCRIPTAR PDF =====
    reader = PdfReader(temp)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.encrypt(password)

    with open(final, "wb") as f:
        writer.write(f)

    os.remove(temp)

    return final
