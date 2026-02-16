from flask import Flask, render_template_string, request, jsonify
import os
import sys

# Agregamos la ruta actual para que encuentre a Shellie
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)
cerebro = None

# INTENTO DE CARGAR EL CORAZÓN DE LUIS STEVEN
try:
    import shellie
    if hasattr(shellie, 'Shellie'):
        cerebro = shellie.Shellie()
    else:
        cerebro = shellie
except Exception as e:
    print(f"Aviso: shellie.py no cargado aún: {e}")

# --- TU CONFIGURACIÓN REAL ---
# (He dejado el link de descarga vacío para que tú pegues el tuyo de Mediafire)
LINK_DESCARGA = "https://www.mediafire.com/file/xmzkq3gu0qh13z2/Shellie_IA.zip/file" 

@app.route('/')
def index():
    return render_template_string(HTML_WEB_FINAL)

@app.route('/chat_real', methods=['POST'])
def chat():
    datos = request.json
    pregunta = datos.get("msg", "")
    
    if cerebro:
        try:
            # Usamos la función hablar de Luis Steven
            if hasattr(cerebro, 'hablar'):
                cerebro.hablar(pregunta)
                respuesta = getattr(cerebro, 'texto_objetivo', "Shellie está pensando...")
            else:
                respuesta = "El archivo shellie.py existe pero no tiene la función hablar."
        except Exception as e:
            respuesta = f"Error en las neuronas: {e}"
    else:
        respuesta = "Shellie no está conectada. Verifica que shellie.py esté en la raíz."

    return jsonify({"respuesta": str(respuesta)})

# --- DISEÑO PROFESIONAL (ESTILO CLIPPY IA) ---
HTML_WEB_FINAL = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Shellie IA | Oficial</title>
    <style>
        :root {{ --neon: #00ffcc; --bg: #0d1117; }}
        body {{ background: var(--bg); color: white; font-family: 'Segoe UI', sans-serif; margin: 0; }}
        nav {{ background: #161b22; padding: 15px 30px; display: flex; gap: 25px; border-bottom: 2px solid var(--neon); }}
        nav a {{ color: #8b949e; text-decoration: none; font-weight: bold; cursor: pointer; text-transform: uppercase; font-size: 13px; }}
        nav a:hover, .activa {{ color: var(--neon) !important; }}
        .seccion {{ display: none; padding: 40px; text-align: center; }}
        .visible {{ display: flex; flex-direction: column; align-items: center; }}
        #chat-window {{ width: 90%; max-width: 650px; height: 400px; background: #1c2128; border-radius: 12px; border: 1px solid #30363d; padding: 20px; overflow-y: auto; text-align: left; margin-bottom: 20px; }}
        input {{ width: 90%; max-width: 650px; padding: 15px; border-radius: 10px; border: 1px solid #30363d; background: #0d1117; color: white; outline: none; }}
        .btn-dl {{ background: var(--neon); color: black; padding: 15px 35px; border-radius: 50px; text-decoration: none; font-weight: bold; margin-top: 20px; }}
    </style>
</head>
<body>
    <nav>
        <a onclick="ir('inicio')" id="l-inicio" class="activa">Inicio</a>
        <a onclick="ir('chat')" id="l-chat">Chat</a>
        <a onclick="ir('descargas')" id="l-descargas">Descargas</a>
    </nav>
    <div id="inicio" class="seccion visible">
        <h1 style="font-size: 3em;">SHELLIE <span style="color:var(--neon)">IA</span></h1>
        <p style="color:#8b949e">Soy Un Clip Con Sentimientos, Soy Shellie.</p>
    </div>
    <div id="chat" class="seccion">
        <div id="chat-window" id="win">
            <div style="color:var(--neon)"><b>Shellie:</b> Sistema activo. ¿En qué puedo ayudarte?</div>
        </div>
        <input type="text" id="userInput" placeholder="Escribe un mensaje..." onkeypress="if(event.key==='Enter') enviar()">
    </div>
    <div id="descargas" class="seccion">
        <h2>Área de Descargas</h2>
        <a href="{LINK_DESCARGA}" class="btn-dl">DESCARGAR APP (.ZIP)</a>
    </div>
    <script>
        function ir(id) {{
            document.querySelectorAll('.seccion').forEach(s => s.classList.remove('visible'));
            document.querySelectorAll('nav a').forEach(a => a.classList.remove('activa'));
            document.getElementById(id).classList.add('visible');
            document.getElementById('l-' + id).classList.add('activa');
        }}
        async function enviar() {{
            let input = document.getElementById('userInput');
            let win = document.getElementById('chat-window');
            let texto = input.value.trim();
            if(!texto) return;
            win.innerHTML += `<div><b>Tú:</b> ${{texto}}</div>`;
            input.value = "";
            let res = await fetch('/chat_real', {{
                method: 'POST',
                headers: {{'Content-Type': 'application/json'}},
                body: JSON.stringify({{msg: texto}})
            }});
            let data = await res.json();
            win.innerHTML += `<div style="color:var(--neon)"><b>Shellie:</b> ${{data.respuesta}}</div>`;
            win.scrollTop = win.scrollHeight;
        }}
    </script>
</body>
</html>
"""

if __name__ == "__main__":
    # Esto es para que funcione en local y en la nube
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)