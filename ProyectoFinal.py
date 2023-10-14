from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = {}

@app.route('/crear-usuario', methods=['POST'])
def crear_usuario():
    datos_usuario = request.get_json()
    nombre_usuario = datos_usuario.get('nombre_usuario')
    contrasena = datos_usuario.get('contrasena')
    if nombre_usuario in usuarios:
        return 'El nombre de usuario ya existe', 400
    usuarios[nombre_usuario] = contrasena
    return 'Usuario creado exitosamente'

@app.route('/iniciar-sesion', methods=['POST'])
def iniciar_sesion():
    datos_usuario = request.get_json()
    nombre_usuario = datos_usuario.get('nombre_usuario')
    contrasena = datos_usuario.get('contrasena')
    if nombre_usuario in usuarios and usuarios[nombre_usuario] == contrasena:
        return 'Inicio de sesión exitoso'
    return 'Nombre de usuario o contraseña incorrectos', 401

if __name__ == '__main__':
    app.run(debug=True)
