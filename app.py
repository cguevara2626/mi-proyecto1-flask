from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta principal: Página de inicio
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para saludar al usuario
@app.route('/saludar')
def saludar():
    nombre = request.args.get('nombre', 'Invitado')  # Obtiene el parámetro 'nombre' de la URL
    return f"¡Hola, {nombre}!"

if __name__ == '__main__':
    app.run(debug=True)
