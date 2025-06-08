'''
RESUMEN NÚMERO DE PUBLICACIONES POR MES Y FORMATO DE PUBLICACIÓN
MES ---   POST --- STORY --- REEL --- LIVE
-------------------------------------------------------
ENERO      1        15        0        1
FEBRERO    0         0        0        0
MARZO      9        40        4        1
ABRIL     15        54        8        0 
MAYO      11        27        5        0
JUNIO     


RESUMEN	TOTAL LIKE Y FORMATO DE PUBLICACIÓN (POST, STORY, REEL & LIVE)
----------------------------		
POST  ---  STORY  ---  REEL  ---  LIVE
2163	   393	       956	      117
'''



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Datos
data_pub = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
    'Post': [1, 0, 9, 15, 11],
    'Story': [15, 0, 40, 54, 27],
    'Reel': [0, 0, 4, 8, 5],
    'Live': [1, 0, 1, 0, 0]
}

df_pub = pd.DataFrame(data_pub)

# Total publicaciones por formato y por mes
total_pub_format = df_pub[['Post', 'Story', 'Reel', 'Live']].sum()
df_pub['Total_Publicaciones'] = df_pub[['Post', 'Story', 'Reel', 'Live']].sum(axis=1)

# Likes
likes = {
    'Formato': ['Post', 'Story', 'Reel', 'Live'],
    'Likes': [2163, 393, 956, 117]
}
df_likes = pd.DataFrame(likes)

# Engagement promedio
engagement = []
for formato in df_likes['Formato']:
    total_pub = total_pub_format[formato]
    total_likes = df_likes.loc[df_likes['Formato'] == formato, 'Likes'].values[0]
    promedio = total_likes / total_pub if total_pub > 0 else 0
    engagement.append(round(promedio, 2))

df_likes['Promedio_Likes_x_Publicación'] = engagement

# ------------- Gráfico 1: Barras agrupadas + línea total correcta --------------
fig, ax1 = plt.subplots(figsize=(10,6))

bar_width = 0.2
x = np.arange(len(df_pub))

# Barras agrupadas
ax1.bar(x - 1.5*bar_width, df_pub['Post'], width=bar_width, label='Post')
ax1.bar(x - 0.5*bar_width, df_pub['Story'], width=bar_width, label='Story')
ax1.bar(x + 0.5*bar_width, df_pub['Reel'], width=bar_width, label='Reel')
ax1.bar(x + 1.5*bar_width, df_pub['Live'], width=bar_width, label='Live')

ax1.set_xticks(x)
ax1.set_xticklabels(df_pub['Mes'], rotation=0)
ax1.set_ylabel('Cantidad de Publicaciones')
ax1.set_xlabel('Mes')
ax1.set_title('Número de Publicaciones por Mes y Formato (Barras Agrupadas)')
ax1.legend(loc='upper left')

# Segundo eje para línea total
ax2 = ax1.twinx()
ax2.plot(x, df_pub['Total_Publicaciones'], color='black', marker='o', label='Total de Publicaciones')
ax2.set_ylabel('Total de Publicaciones')
ax2.set_ylim(0, max(df_pub['Total_Publicaciones']) * 1.1)  # Aquí forzamos que el eje empiece en 0
ax2.legend(loc='upper right')

plt.tight_layout()
plt.show()

# ------------- Gráfico 2: Likes totales + línea promedio likes corregida --------------
fig, ax1 = plt.subplots(figsize=(8,5))

sns.barplot(data=df_likes, x='Formato', y='Likes', ax=ax1, color='skyblue')
ax1.set_ylabel('Likes Totales')
ax1.set_xlabel('Formato')
ax1.set_title('Likes Totales y Engagement Promedio por Formato')
ax1.tick_params(axis='x', rotation=0)

# Segundo eje para promedio likes por publicación
ax2 = ax1.twinx()
x_pos = np.arange(len(df_likes))
ax2.plot(x_pos, df_likes['Promedio_Likes_x_Publicación'], color='red', marker='o', label='Promedio Likes x Publicación')
ax2.set_ylabel('Promedio Likes por Publicación')
ax2.set_ylim(0, max(df_likes['Promedio_Likes_x_Publicación']) * 1.1)  # Aquí forzamos que el eje empiece en 0
ax2.legend(loc='upper right')

plt.tight_layout()
plt.show()

# Impresión estadística
print("Total de publicaciones por formato:")
print(total_pub_format)
print("\nTotal de publicaciones por mes:")
print(df_pub[['Mes', 'Total_Publicaciones']])
print("\nResumen de Engagement:")
print(df_likes)
