# Análisis de datos con pandas y matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo CSV con pandas
try:
    df = pd.read_csv("datos.csv")
    print("Archivo 'datos.csv' cargado exitosamente")
    print(f"Dimensiones del dataset: {df.shape}")
    print(f"Columnas disponibles: {list(df.columns)}")
    print()
except FileNotFoundError:
    print("Error: No se encontró el archivo 'datos.csv'")
    exit()
except Exception as e:
    print(f"Error al cargar el archivo: {e}")
    exit()

# Calcular estadísticas básicas
print("=" * 50)
print("ESTADÍSTICAS DESCRIPTIVAS")
print("=" * 50)

print("\nEstadísticas de col1:")
print(f"Media: {df['col1'].mean():.2f}")
print(f"Mediana: {df['col1'].median():.2f}")
print(f"Desviación estándar: {df['col1'].std():.2f}")
print(f"Mínimo: {df['col1'].min():.2f}")
print(f"Máximo: {df['col1'].max():.2f}")

print("\nEstadísticas de col2:")
print(f"Media: {df['col2'].mean():.2f}")
print(f"Mediana: {df['col2'].median():.2f}")
print(f"Desviación estándar: {df['col2'].std():.2f}")
print(f"Mínimo: {df['col2'].min():.2f}")
print(f"Máximo: {df['col2'].max():.2f}")

# Crear gráfico de dispersión
print("\n" + "=" * 50)
print("GENERANDO GRÁFICO DE DISPERSIÓN")
print("=" * 50)

plt.figure(figsize=(10, 6))
plt.scatter(df["col1"], df["col2"], alpha=0.7, s=50)
plt.title("Gráfico de dispersión: col1 vs col2", fontsize=14, fontweight='bold')
plt.xlabel("col1", fontsize=12)
plt.ylabel("col2", fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("Análisis completado exitosamente!")



