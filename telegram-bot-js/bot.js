const TelegramBot = require('node-telegram-bot-api');
const axios = require('axios');
const { BOT_TOKEN, API_BASE_URL } = require('./config');

// Crear bot
const bot = new TelegramBot(BOT_TOKEN, { polling: true });
console.log("🤖 Bot corriendo...");

// ---------------- Comando /start ----------------
bot.onText(/\/start/, (msg) => {
    const chatId = msg.chat.id;
    const mensaje = `
Bienvenido al Bot del Proyecto APIs

Comandos disponibles:
/usuarios
/categorias
/articulos
/revisores
/revisiones
/comentarios
/favoritos
/biblioteca
/etiquetas
/articulo_etiqueta
`;
    bot.sendMessage(chatId, mensaje);
});

// ---------------- Función genérica para llamar APIs ----------------
async function fetchAPI(endpoint) {
    try {
        const res = await axios.get(`${API_BASE_URL}/${endpoint}`);
        return res.data;
    } catch (err) {
        console.error(err);
        return null;
    }
}

// ---------------- Comandos ----------------
const comandos = [
    { cmd: 'usuarios', endpoint: 'app1/usuario/', format: (data) => {
        if (!data || data.length === 0) return "No hay usuarios.";
        return "Usuarios:\n" + data.map(u => `- ${u.nombre} (${u.tipo_usuario})`).join('\n');
    }},
    { cmd: 'categorias', endpoint: 'app2/categoria/', format: (data) => {
        if (!data || data.length === 0) return "No hay categorías.";
        return "Categorías:\n" + data.map(c => `- ${c.nombre}`).join('\n');
    }},
    { cmd: 'articulos', endpoint: 'app3/articulo/', format: (data) => {
        if (!data || data.length === 0) return "No hay artículos.";
        return "Artículos:\n" + data.map(a => `- ${a.titulo} (visitas: ${a.visitas})`).join('\n');
    }},
    { cmd: 'revisores', endpoint: 'app4/revisor/', format: (data) => {
        if (!data || data.length === 0) return "No hay revisores.";
        return "Revisores:\n" + data.map(r => `- Usuario ID ${r.usuario} | Área: ${r.area_expertise}`).join('\n');
    }},
    { cmd: 'revisiones', endpoint: 'app5/revision/', format: (data) => {
        if (!data || data.length === 0) return "No hay revisiones.";
        return "Revisiones:\n" + data.map(r => `- Artículo ${r.articulo} | Nota: ${r.calificacion}`).join('\n');
    }},
    { cmd: 'comentarios', endpoint: 'app6/comentario/', format: (data) => {
        if (!data || data.length === 0) return "No hay comentarios.";
        return "Comentarios:\n" + data.map(c => `- ${c.contenido.slice(0, 40)}...`).join('\n');
    }},
    { cmd: 'favoritos', endpoint: 'app7/favorito/', format: (data) => {
        if (!data || data.length === 0) return "No hay favoritos.";
        return "Favoritos:\n" + data.map(f => `- Usuario ${f.usuario} → Artículo ${f.articulo}`).join('\n');
    }},
    { cmd: 'biblioteca', endpoint: 'app8/biblioteca/', format: (data) => {
        if (!data || data.length === 0) return "Biblioteca vacía.";
        return "Biblioteca:\n" + data.map(b => `- ${b.titulo} (${b.tipo_recurso})`).join('\n');
    }},
    { cmd: 'etiquetas', endpoint: 'app9/etiqueta/', format: (data) => {
        if (!data || data.length === 0) return "No hay etiquetas.";
        return "Etiquetas:\n" + data.map(e => `- ${e.nombre}`).join('\n');
    }},
    { cmd: 'articulo_etiqueta', endpoint: 'app10/artieti/', format: (data) => {
        if (!data || data.length === 0) return "No hay relaciones artículo-etiqueta.";
        return "Artículo - Etiqueta:\n" + data.map(a => `- Artículo ${a.articulo} ↔ Etiqueta ${a.etiqueta}`).join('\n');
    }}
];

// Registrar los comandos automáticamente
comandos.forEach(({ cmd, endpoint, format }) => {
    bot.onText(new RegExp(`\/${cmd}`), async (msg) => {
        const chatId = msg.chat.id;
        const data = await fetchAPI(endpoint);
        const mensaje = format(data);
        bot.sendMessage(chatId, mensaje);
    });
});
