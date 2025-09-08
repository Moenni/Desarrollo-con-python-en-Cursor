from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import os

# Crear la instancia de la aplicación Flask
app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'  # Cambia esto por una clave segura

# Configuración de la aplicación
app.config['DEBUG'] = True

# Datos de ejemplo (en una aplicación real, esto vendría de una base de datos)
usuarios = [
    {'id': 1, 'nombre': 'Juan Pérez', 'email': 'juan@ejemplo.com'},
    {'id': 2, 'nombre': 'María García', 'email': 'maria@ejemplo.com'},
    {'id': 3, 'nombre': 'Carlos López', 'email': 'carlos@ejemplo.com'}
]

# Rutas de la aplicación
@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html', titulo='Inicio')

@app.route('/usuarios')
def lista_usuarios():
    """Lista todos los usuarios"""
    return render_template('usuarios.html', usuarios=usuarios, titulo='Lista de Usuarios')

@app.route('/usuario/<int:user_id>')
def ver_usuario(user_id):
    """Muestra los detalles de un usuario específico"""
    usuario = next((u for u in usuarios if u['id'] == user_id), None)
    if usuario:
        return render_template('usuario.html', usuario=usuario, titulo=f'Usuario: {usuario["nombre"]}')
    else:
        flash('Usuario no encontrado', 'error')
        return redirect(url_for('lista_usuarios'))

@app.route('/agregar_usuario', methods=['GET', 'POST'])
def agregar_usuario():
    """Agrega un nuevo usuario"""
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        
        if nombre and email:
            nuevo_usuario = {
                'id': len(usuarios) + 1,
                'nombre': nombre,
                'email': email
            }
            usuarios.append(nuevo_usuario)
            flash('Usuario agregado exitosamente', 'success')
            return redirect(url_for('lista_usuarios'))
        else:
            flash('Por favor completa todos los campos', 'error')
    
    return render_template('agregar_usuario.html', titulo='Agregar Usuario')

@app.route('/api/usuarios')
def api_usuarios():
    """API endpoint para obtener usuarios en formato JSON"""
    return jsonify(usuarios)

@app.route('/api/usuario/<int:user_id>')
def api_usuario(user_id):
    """API endpoint para obtener un usuario específico en formato JSON"""
    usuario = next((u for u in usuarios if u['id'] == user_id), None)
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({'error': 'Usuario no encontrado'}), 404

# Manejo de errores
@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('error.html', 
                         error='Página no encontrada', 
                         codigo=404, 
                         titulo='Error 404'), 404

@app.errorhandler(500)
def error_interno(error):
    return render_template('error.html', 
                         error='Error interno del servidor', 
                         codigo=500, 
                         titulo='Error 500'), 500

# Función para ejecutar la aplicación
if __name__ == '__main__':
    print("Iniciando la aplicación Flask...")
    print("Visita http://127.0.0.1:5000 en tu navegador")
    app.run(host='127.0.0.1', port=5000, debug=True)
