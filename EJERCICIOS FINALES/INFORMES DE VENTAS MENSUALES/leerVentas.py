import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#leer archivo
df =pd.read_csv("ventas.csv",parse_dates=["fecha"])

#Crear columnas de ingresos

df["ingresos"]= df["cantidad_vendida"]*df["precio"]

#Extraer el mes

df["mes"]= df["fecha"].dt.to_period("M")

#ventas totales por mes
ventas_por_mes= df.groupby("mes")["ingresos"].sum()
print(ventas_por_mes)

#Producto mas vendido y con mayores ingresos
producto_mas_vendido = df.groupby("producto")["cantidad_vendida"].sum().idxmax()

#Producto con mayores ingresos
producto_mayores_ingresos = df.groupby("producto")["ingresos"].sum().idxmax()
print("Producto mas vendido fue: ",producto_mas_vendido)
print("Producto con mayores ingresos fue: ", producto_mayores_ingresos)

#Gráfico de ventas por mes
ventas_por_mes.plot(kind="bar",title="Ventas Totales por Mes")
plt.ylabel("Ingresos")
plt.xlabel("Mes")
plt.tight_layout()
plt.show()

#Top 5 productos por ingresos
top_productos= df.groupby("producto")["ingresos"].sum().nlargest(5)
top_productos.plot(kind="bar",title="Top 5 productos por Ingresos",color="skyblue")
plt.ylabel("Ingresos")
plt.xlabel("Producto")
plt.tight_layout()
plt.show()