# 📁 Organizador de Archivos

Un sistema automatizado para organizar archivos en carpetas según su tipo de extensión, diseñado para mantener orden en la carpeta de descargas.

## 🚀 Características

- **Clasificación automática** de archivos por tipo de extensión
- **Organización en categorías**: Imágenes, Documentos, Videos y Otros
- **Ejecución manual** o **automatizada** con tareas programadas
- **Logging** de actividades con timestamps
- **Scripts de instalación** y configuración automática

## 📂 Estructura de Carpetas

El organizador crea automáticamente las siguientes carpetas:
- `Imagenes/` - Para archivos .jpg, .jpeg, .png, .gif
- `Documentos/` - Para archivos .pdf, .docx, .txt, .xlsx
- `Videos/` - Para archivos .mp4, .avi, .mov, .mkv
- `Otros/` - Para archivos con extensiones no clasificadas

## 📋 Archivos del Proyecto

### Scripts Python
- **`organizador.py`** - Versión básica para ejecución manual
- **`organizador_automatico.py`** - Versión con automatización y logging

### Scripts de Configuración
- **`instalar_dependencias.bat`** - Instala las librerías necesarias
- **`auto_organizador.bat`** - Ejecuta el organizador manualmente
- **`configurar_tarea.bat`** - Configura tarea automática cada 30 minutos

## 🛠️ Instalación y Uso

### 1. Instalar Dependencias
```bash
# Ejecutar el script de instalación
instalar_dependencias.bat
```

### 2. Uso Manual
```bash
# Ejecutar organizador básico
python organizador.py

# O usar el script batch
auto_organizador.bat
```

### 3. Configurar Automatización
```bash
# Configurar tarea automática (cada 30 minutos)
configurar_tarea.bat
```

### 4. Uso Automático
```bash
# Ejecutar organizador con automatización
python organizador_automatico.py
```

## ⚙️ Configuración

### Modificar Tipos de Archivos
Edita el diccionario `tipos` en los archivos Python para agregar nuevas extensiones:

```python
tipos = {
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"]
}
```

### Cambiar Frecuencia de Ejecución
En `organizador_automatico.py`, modifica las líneas de schedule:

```python
# Cada 30 minutos (actual)
schedule.every(30).minutes.do(ejecutar_organizacion)

# Cada hora
schedule.every().hour.do(ejecutar_organizacion)

# Diario a las 9:00 AM
schedule.every().day.at("09:00").do(ejecutar_organizacion)
```

## 📊 Funcionalidades

- ✅ **Clasificación automática** por extensión de archivo
- ✅ **Creación automática** de carpetas de destino
- ✅ **Manejo de errores** con logging detallado
- ✅ **Contador de archivos** movidos
- ✅ **Timestamps** en todas las operaciones
- ✅ **Configuración flexible** de tipos de archivo
- ✅ **Automatización** con tareas programadas de Windows

## 🔧 Requisitos

- Python 3.x
- Librería `schedule` (para automatización)
- Windows (para scripts .bat y tareas programadas)

## 📝 Notas

- El organizador trabaja sobre la carpeta `descargas/` por defecto
- Los archivos se **mueven** (no copian) a las carpetas de destino
- La carpeta `Otros/` contiene archivos con extensiones no reconocidas
- Las tareas automáticas se pueden gestionar desde el Programador de Tareas de Windows

## 🚨 Advertencias

- **Haz backup** de archivos importantes antes de usar
- El organizador **mueve** archivos, no los copia
- Verifica que la ruta de la carpeta `descargas` sea correcta
- Las tareas automáticas requieren permisos de administrador
