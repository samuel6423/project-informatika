from flask import Flask, request, send_file, jsonify
import io
import ves # Importujeme tvoj kód z ves.py

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('index.html')
    
@app.route('/style.css')
def style():
    return send_file('style.css')
    
@app.route('/script.js')
def script():
    return send_file('script.js')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    ves_input = data.get('ves_input', '')
    
    if not ves_input:
        return jsonify({"error": "Nebol zadaný žiadny text"}), 400
        
    try:
        # Použijeme funkciu render_ves z tvojho ves.py na vygenerovanie obrázka
        # Táto funkcia vráti priamo PIL.Image objekt
        img = ves.render_ves(ves_input)
        
        if img is None:
            return jsonify({"error": "Nepodarilo sa vygenerovať obrázok. Skontroluj formát VES kódu."}), 400
            
        # Uložíme vygenerovaný obrázok do pamäte (bez nutnosti ho ukladať na disk)
        img_io = io.BytesIO()
        img.save(img_io, 'PNG')
        img_io.seek(0)
        
        # Odošleme obrázok naspäť do webovej stránky
        return send_file(img_io, mimetype='image/png')
            
    except Exception as e:
        return jsonify({"error": f"Chyba pri generovaní vo ves.py: {e}"}), 500

if __name__ == '__main__':
    print("Server beží na adrese: http://127.0.0.1:5001")
    app.run(debug=True, port=5001)
