from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import BOT_TOKEN, API_BASE_URL
import requests

print("🤖 Bot corriendo...")

app = ApplicationBuilder().token(BOT_TOKEN).build()

# ---------------- START ----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        " Bienvenido al Bot del Proyecto APIs\n\n"
        "Comandos disponibles:\n"
        "/usuarios\n"
        "/categorias\n"
        "/articulos\n"
        "/revisores\n"
        "/revisiones\n"
        "/comentarios\n"
        "/favoritos\n"
        "/biblioteca\n"
        "/etiquetas\n"
        "/articulo_etiqueta"
    )

# ---------------- API 1 ----------------
async def usuarios(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = requests.get(f"{API_BASE_URL}/app1/usuario/").json()
    if not data:
        await update.message.reply_text("No hay usuarios.")
        return
    msg = " Usuarios:\n"
    for u in data:
        msg += f"- {u['nombre']} ({u['tipo_usuario']})\n"
    await update.message.reply_text(msg)

# ---------------- API 2 ----------------
async def categorias(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = requests.get(f"{API_BASE_URL}/app2/categoria/").json()
    if not data:
        await update.message.reply_text("No hay categorías.")
        return
    msg = " Categorías:\n"
    for c in data:
        msg += f"- {c['nombre']}\n"
    await update.message.reply_text(msg)

# ---------------- API 3 ----------------
async def articulos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = requests.get(f"{API_BASE_URL}/app3/articulo/").json()
    if not data:
        await update.message.reply_text("No hay artículos.")
        return
    msg = " Artículos:\n"
    for a in data:
        msg += f"- {a['titulo']} (visitas: {a['visitas']})\n"
    await update.message.reply_text(msg)

# ---------------- API 4 ----------------
async def revisores(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = requests.get(f"{API_BASE_URL}/app4/revisor/").json()
    if not data:
        await update.message.reply_text("No hay revisores.")
        return
    msg = " Revisores:\n"
    for r in data:
        msg += f"- Usuario ID {r['usuario']} | Área: {r['area_expertise']}\n"
    await update.message.reply_text(msg)

# ---------------- API 5 ----------------
async def revisiones(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = requests.get(f"{API_BASE_URL}/app5/revision/").json()
    if not data:
        await update.message.reply_text("No hay revisiones.")
        return
    msg = " Revisiones:\n"
    for r in data:
        msg += f"- Artículo {r['articulo']} | Nota: {r['calificacion']}\n"
    await update.message.reply_text(msg)

# ---------------- API 6 ----------------
async def comentarios(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = requests.get(f"{API_BASE_URL}/app6/comentario/").json()
    if not data:
        await update.message.reply_text("No hay comentarios.")
        return
    msg = " Comentarios:\n"
    for c in data:
        msg += f"- {c['contenido'][:40]}...\n"
    await update.message.reply_text(msg)

# ---------------- API 7 ----------------
async def favoritos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = requests.get(f"{API_BASE_URL}/app7/favorito/").json()
    if not data:
        await update.message.reply_text("No hay favoritos.")
        return
    msg = " Favoritos:\n"
    for f in data:
        msg += f"- Usuario {f['usuario']} → Artículo {f['articulo']}\n"
    await update.message.reply_text(msg)

# ---------------- API 8 ----------------
async def biblioteca(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = requests.get(f"{API_BASE_URL}/app8/biblioteca/").json()
    if not data:
        await update.message.reply_text("Biblioteca vacía.")
        return
    msg = " Biblioteca:\n"
    for b in data:
        msg += f"- {b['titulo']} ({b['tipo_recurso']})\n"
    await update.message.reply_text(msg)

# ---------------- API 9 ----------------
async def etiquetas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = requests.get(f"{API_BASE_URL}/app9/etiqueta/").json()
    if not data:
        await update.message.reply_text("No hay etiquetas.")
        return
    msg = " Etiquetas:\n"
    for e in data:
        msg += f"- {e['nombre']}\n"
    await update.message.reply_text(msg)

# ---------------- API 10 ----------------
async def articulo_etiqueta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = requests.get(f"{API_BASE_URL}/app10/artieti/").json()
    if not data:
        await update.message.reply_text("No hay relaciones artículo-etiqueta.")
        return
    msg = " Artículo - Etiqueta:\n"
    for a in data:
        msg += f"- Artículo {a['articulo']} ↔ Etiqueta {a['etiqueta']}\n"
    await update.message.reply_text(msg)

# -------- REGISTRO DE COMANDOS --------
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("usuarios", usuarios))
app.add_handler(CommandHandler("categorias", categorias))
app.add_handler(CommandHandler("articulos", articulos))
app.add_handler(CommandHandler("revisores", revisores))
app.add_handler(CommandHandler("revisiones", revisiones))
app.add_handler(CommandHandler("comentarios", comentarios))
app.add_handler(CommandHandler("favoritos", favoritos))
app.add_handler(CommandHandler("biblioteca", biblioteca))
app.add_handler(CommandHandler("etiquetas", etiquetas))
app.add_handler(CommandHandler("articulo_etiqueta", articulo_etiqueta))

# -------- EJECUCIÓN --------
app.run_polling()
