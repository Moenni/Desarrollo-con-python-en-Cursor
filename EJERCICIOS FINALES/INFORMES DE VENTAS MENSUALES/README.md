# 📊 Informes de Ventas Mensuales

## Descripción del Proyecto

Este proyecto es una herramienta de análisis de datos de ventas que permite generar informes mensuales detallados y visualizaciones gráficas para el seguimiento del rendimiento comercial.

## 🚀 Funcionalidades

- **Análisis de ventas por mes**: Calcula los ingresos totales agrupados por período mensual
- **Identificación de productos destacados**: 
  - Producto más vendido por cantidad
  - Producto con mayores ingresos
- **Visualizaciones interactivas**:
  - Gráfico de barras de ventas mensuales
  - Top 5 productos por ingresos
- **Procesamiento de datos**: Lectura y transformación de archivos CSV con fechas

## 📁 Estructura del Proyecto

```
INFORMES DE VENTAS MENSUALES/
├── leerVentas.py      # Script principal de análisis
├── ventas.csv         # Archivo de datos de ventas
├── requirements.txt   # Dependencias del proyecto
└── README.md         # Este archivo
```

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**
- **Pandas**: Manipulación y análisis de datos
- **Matplotlib**: Generación de gráficos
- **Seaborn**: Visualizaciones estadísticas mejoradas

## 📋 Requisitos

Para ejecutar el proyecto, instala las dependencias:

```bash
pip install -r requirements.txt
```

## 🎯 Uso

1. Coloca tu archivo de datos de ventas en formato CSV con las columnas:
   - `fecha`: Fecha de la venta
   - `producto`: Nombre del producto
   - `cantidad_vendida`: Cantidad vendida
   - `precio`: Precio unitario

2. Ejecuta el script:
   ```bash
   python leerVentas.py
   ```

3. El programa generará:
   - Resumen de ventas por mes en consola
   - Identificación de productos destacados
   - Gráficos de visualización automáticos

## 📈 Características del Análisis

- **Cálculo automático de ingresos**: Multiplica cantidad vendida por precio
- **Agrupación temporal**: Extrae el mes de las fechas para análisis mensual
- **Métricas de rendimiento**: Identifica productos líderes en ventas e ingresos
- **Visualizaciones claras**: Gráficos de barras para fácil interpretación

## 📊 Ejemplo de Salida

El programa mostrará:
- Ventas totales por mes
- Producto más vendido
- Producto con mayores ingresos
- Gráfico de ventas mensuales
- Top 5 productos por ingresos

---

*Proyecto desarrollado como parte del curso de Python con Cursor*
