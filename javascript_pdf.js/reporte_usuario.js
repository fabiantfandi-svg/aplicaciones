const fs = require("fs");
const path = require("path");
const { PDFDocument, StandardFonts } = require("pdf-lib");
const nodemailer = require("nodemailer");
const axios = require("axios");

const { API_BASE_URL, EMAIL_USER, EMAIL_PASS } = require("./config");

// ================= GENERAR PDF =================
async function generarPDFUsuario(usuario, articulos, comentarios, favoritos, biblioteca, revisiones) {
    const pdfDoc = await PDFDocument.create();
    const page = pdfDoc.addPage();
    const { width, height } = page.getSize();
    const font = await pdfDoc.embedFont(StandardFonts.Helvetica);
    let y = height - 50;

    function escribirTitulo(texto) {
        page.drawText(texto, { x: 50, y, size: 14, font });
        y -= 20;
    }

    function escribirTexto(texto) {
        page.drawText(texto, { x: 70, y, size: 11, font });
        y -= 15;
    }

    // ===== DATOS DEL USUARIO =====
    escribirTitulo("REPORTE GENERAL DEL USUARIO");
    y -= 10;
    escribirTexto(`Nombre: ${usuario.nombre}`);
    escribirTexto(`Email: ${usuario.email}`);
    y -= 10;

    // ===== ARTÍCULOS =====
    escribirTitulo("Artículos creados");
    if (!articulos.length) escribirTexto("- No hay artículos");
    else articulos.forEach(a => escribirTexto(`- ${a.titulo}`));
    y -= 10;

    // ===== COMENTARIOS =====
    escribirTitulo("Comentarios realizados");
    if (!comentarios.length) escribirTexto("- No hay comentarios");
    else comentarios.forEach(c => escribirTexto(`- ${c.contenido.slice(0, 60)}`));
    y -= 10;

    // ===== FAVORITOS =====
    escribirTitulo("Artículos favoritos");
    if (!favoritos.length) escribirTexto("- No hay favoritos");
    else favoritos.forEach(f => escribirTexto(`- ${f.articulo.titulo}`));
    y -= 10;

    // ===== BIBLIOTECA =====
    escribirTitulo("Recursos subidos a biblioteca");
    if (!biblioteca.length) escribirTexto("- No hay recursos");
    else biblioteca.forEach(b => escribirTexto(`- ${b.titulo}`));
    y -= 10;

    // ===== REVISIONES =====
    escribirTitulo("Revisiones realizadas");
    if (!revisiones.length) escribirTexto("- No hay revisiones");
    else revisiones.forEach(r => escribirTexto(`- Artículo ID ${r.articulo.id_articulo} -> ${r.recomendacion}`));
    y -= 10;

    // ===== GUARDAR PDF =====
    const pdfBytes = await pdfDoc.save();
    const archivoPath = path.join(__dirname, `reporte_usuario_${usuario.id_usuario}.pdf`);
    fs.writeFileSync(archivoPath, pdfBytes);

    return archivoPath;
}

// ================= ENVIAR CORREO =================
async function enviarPDFPorCorreo(destino, archivo) {
    const transporter = nodemailer.createTransport({
        service: "gmail",
        auth: { user: EMAIL_USER, pass: EMAIL_PASS },
    });

    const mailOptions = {
        from: EMAIL_USER,
        to: destino,
        subject: "Reporte de actividad",
        text: `Hola,\n\nAdjunto encontrarás tu reporte personal en PDF.\n\nSaludos,\nSistema Académico`,
        attachments: [{ filename: path.basename(archivo), path: archivo }],
    };

    await transporter.sendMail(mailOptions);
}

// ================= SCRIPT PRINCIPAL =================
(async () => {
    const userId = process.argv[2];
    const correo = process.argv[3];

    if (!userId || !correo) {
        console.log("Uso: node reporte_usuario.js <user_id> <correo>");
        process.exit(1);
    }

    try {
        
        const usuario = (await axios.get(`${API_BASE_URL}/app1/usuarios/${userId}`)).data;
        const articulos   = (await axios.get(`${API_BASE_URL}/app3/articulo/?autor=${userId}`)).data || [];
        const comentarios = (await axios.get(`${API_BASE_URL}/app6/comentario/?usuario=${userId}`)).data || [];
        const favoritos   = (await axios.get(`${API_BASE_URL}/app7/favorito/?usuario=${userId}`)).data || [];
        const biblioteca  = (await axios.get(`${API_BASE_URL}/app8/biblioteca/?subido_por=${userId}`)).data || [];
        const revisiones  = (await axios.get(`${API_BASE_URL}/app5/revision/?revisor__usuario=${userId}`)).data || [];

        const archivoPDF = await generarPDFUsuario(usuario, articulos, comentarios, favoritos, biblioteca, revisiones);
        await enviarPDFPorCorreo(correo, archivoPDF);

        console.log("✅ PDF generado y enviado correctamente");

    } catch (error) {
        if (error.response) {
            console.error(`❌ Error: ${error.response.status} - ${error.response.statusText}`);
        } else {
            console.error("❌ Error:", error.message);
        }
    }
})();
