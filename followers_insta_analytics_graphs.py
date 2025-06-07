'''
MES --- SEGUIDORES
------------------
ENERO     1193
FEBRERO   1214
MARZO     1207
ABRIL     1255
MAYO      1378
JUNIO     1408
'''

'''
Información estadística relevante para el informe:
1. Tendencia de crecimiento de seguidores
      Muestra cómo han cambiado los seguidores mes a mes.
      Puedes calcular el crecimiento mensual en número y en porcentaje.

2. Crecimiento acumulado o total
      Cuánto ha aumentado el total de seguidores desde enero hasta junio.

3. Promedio de seguidores por mes
      Indica el promedio para entender un valor típico.

4. Mes con mayor crecimiento
      Identifica el mes en que hubo más aumento de seguidores.

5. Visualización del comportamiento
      Una gráfica clara que muestre la evolución.
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Datos
datos = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'],
    'Seguidores': [1193, 1214, 1207, 1255, 1378, 1408]
}

df = pd.DataFrame(datos)

# 1. Tendencia de crecimiento mensual (número y porcentaje)
df['Crecimiento'] = df['Seguidores'].diff()  # Diferencia mes a mes
df['Crecimiento %'] = df['Seguidores'].pct_change() * 100  # Porcentaje
df['Crecimiento %'] = df['Crecimiento %'].round(2)

# 2. Crecimiento acumulado o total (de enero a junio)
crecimiento_total = df['Seguidores'].iloc[-1] - df['Seguidores'].iloc[0]

# 3. Promedio de seguidores por mes
promedio_seguidores = df['Seguidores'].mean()

# 4. Mes con mayor crecimiento (en número)
mes_mayor_crecimiento = df.loc[df['Crecimiento'].idxmax(), 'Mes']
valor_mayor_crecimiento = df['Crecimiento'].max()

# Preparar la impresión para mostrar "-" en el primer mes (NaN)
df_imp = df.copy()
df_imp['Crecimiento'] = df_imp['Crecimiento'].fillna('-')
df_imp['Crecimiento %'] = df_imp['Crecimiento %'].fillna('-')

# Resultados
print("Crecimiento mensual (número y porcentaje):")
print(df_imp[['Mes', 'Crecimiento', 'Crecimiento %']].to_string(index=False))
print(f"\nCrecimiento total de seguidores (Enero a Junio): {crecimiento_total} seguidores")
print(f"Promedio de seguidores por mes: {promedio_seguidores:.2f}")
print(f"Mes con mayor crecimiento: {mes_mayor_crecimiento} con {valor_mayor_crecimiento} seguidores adicionales")

# 5. Visualización del comportamiento con línea de tendencia y etiquetas

plt.figure(figsize=(10,6))
plt.plot(df['Mes'], df['Seguidores'], marker='o', linestyle='-', color='b', label='Seguidores')

# Línea de tendencia (regresión lineal)
x = np.arange(len(df))
coef = np.polyfit(x, df['Seguidores'], 1)
poly1d_fn = np.poly1d(coef)
plt.plot(df['Mes'], poly1d_fn(x), color='r', linestyle='--', label='Tendencia')

# Etiquetas con número de seguidores en cada punto
for i, (mes, seg) in enumerate(zip(df['Mes'], df['Seguidores'])):
    plt.text(i, seg + 10, str(seg), ha='center', fontsize=9)

plt.title('Evolución de Seguidores en Instagram (Enero - Junio)')
plt.xlabel('Mes')
plt.ylabel('Número de Seguidores')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
