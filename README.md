# 🐍 SANTANDER PYTHON CON CURSOR

Este repositorio contiene una colección completa de ejercicios prácticos y proyectos de Python desarrollados durante la formación académica con Santander. El proyecto está organizado en módulos progresivos que cubren desde conceptos básicos hasta aplicaciones más avanzadas de análisis de datos.

## 📋 Descripción del Proyecto

Este proyecto forma parte de un programa de formación en Python que abarca diferentes niveles de complejidad, desde ejercicios fundamentales hasta proyectos prácticos de análisis de datos. Cada módulo está diseñado para desarrollar habilidades específicas en programación Python.

## 🗂️ Estructura del Proyecto

```
SANTANDER PYTHON CON CURSOR/
├── README.md                    # Este archivo principal
├── EJERCICIOS PRACTICOS/        # Proyectos integrados y ejercicios avanzados
│   ├── README.md               # Documentación detallada de ejercicios
│   ├── analisisDatos.py        # Análisis estadístico con pandas/matplotlib
│   ├── calculadora.py          # Calculadora interactiva
│   ├── fizzbuzz.py            # Algoritmo FizzBuzz clásico
│   ├── datos.csv              # Dataset de ejemplo
│   └── requirements.txt       # Dependencias del proyecto
├── MODULO1/                    # Conceptos básicos y funciones
│   ├── EJEMPLO.py             # Ejemplo introductorio
│   └── ejercicio_autocompletar.py  # Generación de cuadrados
├── MODULO2/                    # Algoritmos y lógica matemática
│   └── es_primo.py            # Verificación de números primos
├── MODULO3/                    # Procesamiento de archivos y texto
│   └── contador_palabras/     # Proyecto de análisis de texto
│       ├── venv/              # Entorno virtual
│       │   └── contador.ipynb # Jupyter notebook interactivo
│       └── palabras.txt       # Archivo de texto de ejemplo
└── MODULO5/                    # Módulo futuro (en desarrollo)
```

## 🚀 Instalación y Configuración

### Requisitos Previos
- Python 3.7 o superior
- pip (gestor de paquetes de Python)
- Git (para clonar el repositorio)

### Instalación Rápida

```bash
# Clonar el repositorio
git clone [URL_DEL_REPOSITORIO]

# Navegar al directorio principal
cd SANTANDER-PYTHON-CON-CURSOR

# Instalar dependencias para ejercicios prácticos
cd "EJERCICIOS PRACTICOS"
pip install -r requirements.txt
```

### Configuración del Entorno Virtual (Recomendado)

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r "EJERCICIOS PRACTICOS/requirements.txt"
```

## 📚 Contenido por Módulos

### 🎯 MODULO1 - Conceptos Básicos
**Objetivo:** Introducción a Python y programación funcional

#### Ejercicios Incluidos:
- **`EJEMPLO.py`**: Programa introductorio con "Hola Mundo" y bucles básicos
- **`ejercicio_autocompletar.py`**: Función para generar cuadrados de números naturales

#### Desafíos Resueltos:
- ✅ Manejo de entrada de usuario
- ✅ Validación de datos de entrada
- ✅ Programación funcional con type hints
- ✅ Manejo de excepciones (ValueError)
- ✅ List comprehensions para generación de listas

### 🔢 MODULO2 - Algoritmos Matemáticos
**Objetivo:** Implementación de algoritmos matemáticos y lógica de programación

#### Ejercicios Incluidos:
- **`es_primo.py`**: Verificador de números primos con optimización

#### Desafíos Resueltos:
- ✅ Algoritmo de verificación de números primos
- ✅ Optimización matemática (raíz cuadrada)
- ✅ Validación de tipos de datos
- ✅ Manejo de casos especiales (números ≤ 1)
- ✅ Interfaz de usuario interactiva

### 📄 MODULO3 - Procesamiento de Archivos
**Objetivo:** Manipulación de archivos de texto y análisis de contenido

#### Ejercicios Incluidos:
- **`contador_palabras/`**: Proyecto completo de análisis de texto
  - `contador.ipynb`: Jupyter notebook interactivo
  - `palabras.txt`: Archivo de texto de ejemplo

#### Desafíos Resueltos:
- ✅ Lectura de archivos con manejo de encoding UTF-8
- ✅ Procesamiento de texto con expresiones regulares
- ✅ Conteo de palabras y estadísticas
- ✅ Uso de collections.Counter para análisis
- ✅ Identificación de palabras más frecuentes
- ✅ Manejo de errores de archivos no encontrados

### 🚀 EJERCICIOS PRACTICOS - Proyectos Integrados
**Objetivo:** Aplicación de conocimientos en proyectos reales

#### Proyectos Incluidos:

##### 📊 Análisis de Datos (`analisisDatos.py`)
- **Funcionalidad**: Análisis estadístico completo de datasets CSV
- **Tecnologías**: pandas, matplotlib
- **Características**:
  - Carga y procesamiento de archivos CSV
  - Cálculo de estadísticas descriptivas
  - Generación de gráficos de dispersión
  - Manejo robusto de errores

##### 🧮 Calculadora Interactiva (`calculadora.py`)
- **Funcionalidad**: Calculadora de consola con operaciones básicas
- **Características**:
  - Operaciones: suma, resta, multiplicación, división
  - Validación de entrada de datos
  - Manejo de errores (división por cero)
  - Interfaz de usuario interactiva

##### 🔢 FizzBuzz (`fizzbuzz.py`)
- **Funcionalidad**: Implementación clásica del algoritmo FizzBuzz
- **Lógica**:
  - Múltiplos de 3: "Fizz"
  - Múltiplos de 5: "Buzz"
  - Múltiplos de 3 y 5: "FizzBuzz"

#### Desafíos Resueltos:
- ✅ Análisis estadístico con pandas
- ✅ Visualización de datos con matplotlib
- ✅ Programación orientada a funciones
- ✅ Patrones de diseño (diccionario de funciones)
- ✅ Manejo de errores y validación
- ✅ Algoritmos clásicos de programación
- ✅ Interfaz de usuario de consola

## 🛠️ Instrucciones de Uso

### Ejecutar Ejercicios Individuales

```bash
# Módulo 1 - Cuadrados
python "MODULO1/ejercicio_autocompletar.py"

# Módulo 2 - Números primos
python "MODULO2/es_primo.py"

# Módulo 3 - Contador de palabras (Jupyter)
jupyter notebook "MODULO3/contador_palabras/venv/contador.ipynb"
```

### Ejecutar Proyectos Prácticos

```bash
# Navegar a ejercicios prácticos
cd "EJERCICIOS PRACTICOS"

# Análisis de datos
python analisisDatos.py

# Calculadora interactiva
python calculadora.py

# FizzBuzz
python fizzbuzz.py
```

## 📊 Tecnologías y Librerías Utilizadas

### Librerías Principales
- **pandas** (≥2.0.0): Manipulación y análisis de datos
- **matplotlib** (≥3.5.0): Visualización de datos
- **collections**: Estructuras de datos avanzadas
- **re**: Procesamiento de expresiones regulares

### Características de Python
- **Type Hints**: Anotaciones de tipo para mejor documentación
- **List Comprehensions**: Generación eficiente de listas
- **Exception Handling**: Manejo robusto de errores
- **File I/O**: Lectura y escritura de archivos
- **Regular Expressions**: Procesamiento de patrones de texto

## 🎯 Objetivos de Aprendizaje Alcanzados

### Conceptos Fundamentales
- ✅ Sintaxis básica de Python
- ✅ Variables, tipos de datos y estructuras
- ✅ Control de flujo (if, for, while)
- ✅ Funciones y parámetros
- ✅ Manejo de excepciones

### Programación Avanzada
- ✅ Programación funcional
- ✅ Type hints y documentación
- ✅ Algoritmos matemáticos
- ✅ Optimización de código
- ✅ Patrones de diseño

### Análisis de Datos
- ✅ Manipulación de datasets
- ✅ Estadísticas descriptivas
- ✅ Visualización de datos
- ✅ Procesamiento de archivos CSV
- ✅ Análisis de texto

### Herramientas de Desarrollo
- ✅ Entornos virtuales
- ✅ Gestión de dependencias
- ✅ Jupyter Notebooks
- ✅ Control de versiones
- ✅ Documentación de código

## 🔧 Personalización y Extensión

### Agregar Nuevos Ejercicios
1. Crear archivo en el módulo correspondiente
2. Seguir las convenciones de nomenclatura
3. Incluir documentación y type hints
4. Actualizar este README

### Modificar Datasets
1. Reemplazar `datos.csv` con tu dataset
2. Ajustar nombres de columnas en `analisisDatos.py`
3. Verificar formato de datos

### Extender Funcionalidades
1. Agregar nuevas operaciones a la calculadora
2. Implementar más tipos de gráficos
3. Crear nuevos algoritmos de análisis

## 🐛 Solución de Problemas

### Errores Comunes

#### "No module named 'pandas'"
```bash
pip install pandas matplotlib
```

#### "FileNotFoundError"
- Verificar que los archivos estén en las rutas correctas
- Ejecutar desde el directorio apropiado

#### "ValueError" en entrada de usuario
- Verificar que se ingresen números válidos
- Revisar el formato de entrada esperado

## 📝 Notas de Desarrollo

- **Versión de Python**: 3.13
- **Última actualización**: Enero 2025
- **Estilo de código**: PEP 8
- **Documentación**: Docstrings en español
- **Manejo de errores**: Try-except en funciones críticas

## 🤝 Contribuciones

Este es un proyecto educativo. Las contribuciones son bienvenidas:

1. Fork del proyecto
2. Crear una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit de tus cambios (`git commit -m 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abrir un Pull Request

## 📄 Licencia

Este proyecto es parte de la formación académica con Santander y está destinado únicamente para fines educativos.

## 🏆 Logros del Proyecto

- ✅ **15+ ejercicios** implementados exitosamente
- ✅ **4 módulos** de dificultad progresiva
- ✅ **3 proyectos integrados** con funcionalidades completas
- ✅ **Análisis de datos** con visualizaciones profesionales
- ✅ **Manejo robusto de errores** en todos los módulos
- ✅ **Documentación completa** en español
- ✅ **Código limpio** siguiendo estándares PEP 8

---

**Desarrollado con ❤️ durante la formación de Python con Santander**

*Este proyecto demuestra el progreso en el aprendizaje de Python, desde conceptos básicos hasta aplicaciones prácticas de análisis de datos.*
