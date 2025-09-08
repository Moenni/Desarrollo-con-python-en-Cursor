# Aplicación Web con Flask

Una aplicación web simple desarrollada con Flask que demuestra las funcionalidades básicas de un CRUD (Create, Read, Update, Delete) para gestión de usuarios.

## 🚀 Características

- **Interfaz moderna**: Diseño responsive con Bootstrap 5 y Font Awesome
- **Gestión de usuarios**: Lista, visualización y agregado de usuarios
- **API REST**: Endpoints JSON para acceso programático
- **Mensajes flash**: Feedback visual para las acciones del usuario
- **Manejo de errores**: Páginas de error personalizadas (404, 500)
- **Validación de formularios**: Validación tanto en frontend como backend

## 📁 Estructura del Proyecto

```
APLICACION WEB CON FLASK/
├── app.py                 # Aplicación principal de Flask
├── requirements.txt       # Dependencias del proyecto
├── README.md             # Este archivo
├── templates/            # Plantillas HTML
│   ├── base.html         # Plantilla base
│   ├── index.html        # Página de inicio
│   ├── usuarios.html     # Lista de usuarios
│   ├── usuario.html      # Detalles de usuario
│   ├── agregar_usuario.html # Formulario de agregar usuario
│   └── error.html        # Página de errores
└── static/               # Archivos estáticos
    ├── css/
    │   └── style.css     # Estilos personalizados
    └── js/
        └── main.js       # JavaScript personalizado
```

## 🛠️ Instalación y Configuración

### Prerrequisitos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Pasos de instalación

1. **Clona o descarga el proyecto**
   ```bash
   cd "EJERCICIOS FINALES/APLICACION WEB CON FLASK"
   ```

2. **Crea un entorno virtual (recomendado)**
   ```bash
   python -m venv venv
   
   # En Windows:
   venv\Scripts\activate
   
   # En macOS/Linux:
   source venv/bin/activate
   ```

3. **Instala las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecuta la aplicación**
   ```bash
   python app.py
   ```

5. **Abre tu navegador**
   Visita `http://127.0.0.1:5000` en tu navegador web

## 📖 Uso de la Aplicación

### Páginas Disponibles

- **Inicio** (`/`): Página principal con información general
- **Lista de Usuarios** (`/usuarios`): Muestra todos los usuarios registrados
- **Detalles de Usuario** (`/usuario/<id>`): Información detallada de un usuario específico
- **Agregar Usuario** (`/agregar_usuario`): Formulario para agregar nuevos usuarios

### API REST

La aplicación incluye endpoints JSON para acceso programático:

- `GET /api/usuarios` - Obtener todos los usuarios
- `GET /api/usuario/<id>` - Obtener un usuario específico

**Ejemplo de uso de la API:**
```bash
# Obtener todos los usuarios
curl http://127.0.0.1:5000/api/usuarios

# Obtener un usuario específico
curl http://127.0.0.1:5000/api/usuario/1
```

## 🎨 Personalización

### Modificar el diseño

- **CSS**: Edita `static/css/style.css` para cambiar estilos
- **JavaScript**: Modifica `static/js/main.js` para agregar funcionalidades
- **Plantillas**: Actualiza los archivos en `templates/` para cambiar el HTML

### Agregar nuevas funcionalidades

1. **Nuevas rutas**: Agrega funciones en `app.py` con el decorador `@app.route()`
2. **Nuevas plantillas**: Crea archivos HTML en `templates/`
3. **Nuevos estilos**: Añade CSS en `static/css/style.css`

## 🔧 Configuración Avanzada

### Variables de entorno

Puedes crear un archivo `.env` para configuraciones:

```env
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=tu_clave_secreta_muy_segura
DEBUG=True
```

### Modo de producción

Para ejecutar en producción:

```bash
# Con Gunicorn (Linux/macOS)
gunicorn -w 4 -b 0.0.0.0:8000 app:app

# Con Waitress (Windows)
waitress-serve --host=0.0.0.0 --port=8000 app:app
```

## 🐛 Solución de Problemas

### Error: "ModuleNotFoundError: No module named 'flask'"

**Solución**: Asegúrate de haber instalado las dependencias:
```bash
pip install -r requirements.txt
```

### Error: "Address already in use"

**Solución**: El puerto 5000 está ocupado. Cambia el puerto en `app.py`:
```python
app.run(host='127.0.0.1', port=5001, debug=True)
```

### La página no carga

**Solución**: Verifica que la aplicación esté ejecutándose y que uses la URL correcta: `http://127.0.0.1:5000`

## 📚 Recursos Adicionales

- [Documentación oficial de Flask](https://flask.palletsprojects.com/)
- [Bootstrap 5 Documentation](https://getbootstrap.com/docs/5.1/)
- [Font Awesome Icons](https://fontawesome.com/icons)
- [Jinja2 Template Engine](https://jinja.palletsprojects.com/)

## 🤝 Contribuciones

Este es un proyecto de ejemplo para aprendizaje. Si encuentras errores o tienes sugerencias:

1. Identifica el problema
2. Propón una solución
3. Implementa los cambios
4. Prueba la funcionalidad

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 👨‍💻 Autor

Desarrollado como parte del curso de Python con Cursor - Santander.

---

**¡Disfruta explorando la aplicación!** 🎉
