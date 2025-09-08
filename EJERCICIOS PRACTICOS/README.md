# 🐍 Ejercicios Prácticos de Python

Este repositorio contiene una colección de ejercicios prácticos de Python desarrollados durante la formación académica con Santander. Los ejercicios cubren diferentes conceptos fundamentales de programación en Python.

## 📋 Contenido del Proyecto

### 📊 Análisis de Datos (`analisisDatos.py`)
Script completo para análisis estadístico de datos CSV utilizando pandas y matplotlib.

**Características:**
- Carga y procesamiento de archivos CSV
- Cálculo de estadísticas descriptivas (media, mediana, desviación estándar, mínimo, máximo)
- Generación de gráficos de dispersión
- Manejo robusto de errores
- Interfaz de usuario informativa

### 🧮 Calculadora Interactiva (`calculadora.py`)
Calculadora de consola con operaciones básicas matemáticas.

**Funcionalidades:**
- Suma, resta, multiplicación y división
- Validación de entrada de datos
- Manejo de errores (división por cero, entrada inválida)
- Interfaz de usuario interactiva
- Opción de salida del programa

### 🔢 FizzBuzz (`fizzbuzz.py`)
Implementación clásica del algoritmo FizzBuzz para números del 1 al 50.

**Lógica:**
- Múltiplos de 3: "Fizz"
- Múltiplos de 5: "Buzz"  
- Múltiplos de 3 y 5: "FizzBuzz"
- Otros números: se muestran tal como son

### 📈 Datos de Ejemplo (`datos.csv`)
Archivo CSV con datos de muestra para el análisis estadístico.

**Estructura:**
```csv
col1,col2
10,20
15,25
20,30
25,35
30,40
```

## 🚀 Instalación

### Requisitos Previos
- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Dependencias
El proyecto requiere las siguientes librerías:

```bash
pip install pandas matplotlib
```

### Instalación Rápida
```bash
# Clonar el repositorio
git clone [URL_DEL_REPOSITORIO]

# Navegar al directorio
cd EJERCICIOS-PRACTICOS

# Instalar dependencias
pip install -r requirements.txt
```

## 📖 Instrucciones de Uso

### 1. Análisis de Datos
```bash
python analisisDatos.py
```

**Salida esperada:**
- Estadísticas descriptivas de ambas columnas
- Gráfico de dispersión interactivo
- Información del dataset cargado

### 2. Calculadora
```bash
python calculadora.py
```

**Uso:**
1. Ingresa la operación deseada (suma, resta, multiplicacion, division)
2. Ingresa el primer número
3. Ingresa el segundo número
4. Ve el resultado
5. Escribe "salir" para terminar

### 3. FizzBuzz
```bash
python fizzbuzz.py
```

**Salida:**
- Lista de números del 1 al 50 con las reglas FizzBuzz aplicadas

## 🛠️ Estructura del Proyecto

```
EJERCICIOS-PRACTICOS/
├── README.md              # Este archivo
├── analisisDatos.py       # Análisis estadístico con pandas/matplotlib
├── calculadora.py         # Calculadora interactiva
├── fizzbuzz.py           # Algoritmo FizzBuzz
├── datos.csv             # Datos de ejemplo para análisis
└── requirements.txt      # Dependencias del proyecto
```

## 📊 Características Técnicas

### Análisis de Datos
- **Librerías:** pandas, matplotlib
- **Funcionalidades:** Estadísticas descriptivas, visualización de datos
- **Manejo de errores:** Validación de archivos, manejo de excepciones
- **Formato de salida:** Estadísticas con 2 decimales, gráficos profesionales

### Calculadora
- **Patrón de diseño:** Diccionario de funciones
- **Validación:** Entrada numérica, división por cero
- **Interfaz:** Bucle interactivo con opción de salida

### FizzBuzz
- **Algoritmo:** Condicionales anidados
- **Rango:** Números del 1 al 50
- **Lógica:** Múltiplos de 3, 5, y ambos

## 🎯 Objetivos de Aprendizaje

Este proyecto demuestra:
- ✅ Manejo de archivos CSV con pandas
- ✅ Análisis estadístico básico
- ✅ Visualización de datos con matplotlib
- ✅ Programación orientada a funciones
- ✅ Manejo de errores y validación de entrada
- ✅ Algoritmos clásicos de programación
- ✅ Interfaz de usuario de consola
- ✅ Estructuras de datos (diccionarios, listas)

## 🔧 Personalización

### Modificar el Dataset
Para usar tus propios datos:
1. Reemplaza `datos.csv` con tu archivo
2. Asegúrate de que tenga columnas `col1` y `col2`
3. Ejecuta `python analisisDatos.py`

### Extender la Calculadora
Para agregar más operaciones:
1. Define una nueva función matemática
2. Agrega la función al diccionario `operaciones`
3. Actualiza la validación de entrada

## 🐛 Solución de Problemas

### Error: "No module named 'pandas'"
```bash
pip install pandas matplotlib
```

### Error: "FileNotFoundError: datos.csv"
- Verifica que el archivo `datos.csv` esté en el mismo directorio
- Asegúrate de ejecutar el script desde el directorio correcto

### Error: "KeyError: 'col1'"
- Verifica que el CSV tenga las columnas correctas
- Revisa que no haya caracteres especiales en los nombres de columnas

## 📝 Notas de Desarrollo

- **Versión de Python:** 3.13
- **Última actualización:** Enero 2025
- **Formato de código:** PEP 8
- **Manejo de errores:** Try-except en funciones críticas

## 🤝 Contribuciones

Este es un proyecto educativo. Las contribuciones son bienvenidas:
1. Fork del proyecto
2. Crea una rama para tu feature
3. Commit de tus cambios
4. Push a la rama
5. Abre un Pull Request

## 📄 Licencia

Este proyecto es parte de la formación académica con Santander y está destinado únicamente para fines educativos.

---

**Desarrollado con ❤️ durante la formación de Python con Santander**
