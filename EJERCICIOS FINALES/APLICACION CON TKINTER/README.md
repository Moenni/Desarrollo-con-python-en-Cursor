# Aplicación Bloc de Notas con Tkinter

## Descripción

Esta es una aplicación de escritorio desarrollada en Python utilizando la librería Tkinter que implementa un bloc de notas simple y funcional. La aplicación permite crear, abrir y guardar archivos de texto de manera intuitiva a través de una interfaz gráfica.

## Características

- **Interfaz gráfica intuitiva**: Ventana principal con área de texto expandible
- **Funcionalidad de archivos**:
  - Abrir archivos de texto existentes (.txt)
  - Guardar archivos de texto nuevos o modificados
  - Salir de la aplicación
- **Menú superior**: Acceso fácil a todas las funciones principales
- **Compatibilidad con UTF-8**: Soporte completo para caracteres especiales y acentos

## Requisitos del Sistema

- Python 3.x
- Librería Tkinter (incluida por defecto en Python)

## Instalación

No se requiere instalación adicional ya que Tkinter viene incluido con Python por defecto.

## Uso

1. Ejecutar el archivo `api.py`:
   ```bash
   python api.py
   ```

2. La aplicación se abrirá mostrando una ventana con un área de texto vacía

3. Utilizar el menú "Archivo" para:
   - **Abrir**: Seleccionar un archivo de texto existente
   - **Guardar**: Guardar el contenido actual en un archivo
   - **Salir**: Cerrar la aplicación

## Estructura del Proyecto

```
APLICACION CON TKINTER/
├── api.py                    # Archivo principal de la aplicación
├── PRIMER_BORRADOR.txt       # Archivo de notas del desarrollo
└── README.md                 # Este archivo de documentación
```

## Funcionalidades Técnicas

- **Widget Text**: Área de texto multilínea con ajuste automático de palabras
- **FileDialog**: Diálogos nativos del sistema para selección de archivos
- **MessageBox**: Notificaciones al usuario para confirmaciones
- **Menú desplegable**: Interfaz de usuario estándar para operaciones de archivo

## Desarrollo

Este proyecto forma parte de los ejercicios finales del curso de Python, demostrando el uso de Tkinter para crear aplicaciones de escritorio con interfaz gráfica.
