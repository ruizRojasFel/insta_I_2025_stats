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

# Datos: Publicaciones por mes y formato
data_pub = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
    'Post': [1, 0, 9, 15, 11],
    'Story': [15, 0, 40, 54, 27],
    'Reel': [0, 0, 4, 8, 5],
    'Live': [1, 0, 1, 0, 0]
}

df_pub = pd.DataFrame(data_pub)

# Total de publicaciones por formato
total_pub_format = df_pub[['Post', 'Story', 'Reel', 'Live']].sum()

# Total de publicaciones por mes
df_pub['Total_Publicaciones'] = df_pub[['Post', 'Story', 'Reel', 'Live']].sum(axis=1)

# Likes por formato
likes = {
    'Formato': ['Post', 'Story', 'Reel', 'Live'],
    'Likes': [2163, 393, 956, 117]
}

df_likes = pd.DataFrame(likes)

# ---- ANÁLISIS DE ENGAGEMENT (Likes por publicación) ----
engagement = []
for formato in df_likes['Formato']:
    total_pub = total_pub_format[formato]
    total_likes = df_likes[df_likes['Formato'] == formato]['Likes'].values[0]
    promedio = total_likes / total_pub if total_pub > 0 else 0
    engagement.append(round(promedio, 2))

df_likes['Promedio_Likes_x_Publicación'] = engagement

# ------------------ VISUALIZACIONES ---------------------

# 1. Publicaciones por formato
plt.figure(figsize=(8, 5))
total_pub_format.plot(kind='bar', color='skyblue')
plt.title('Total de Publicaciones por Formato (Ene - May)')
plt.ylabel('Cantidad')
plt.xlabel('Formato')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 2. Publicaciones por mes (apilado por formato)
df_pub_plot = df_pub.set_index('Mes')[['Post', 'Story', 'Reel', 'Live']]
df_pub_plot.plot(kind='bar', stacked=True, figsize=(10,6), colormap='viridis')
plt.title('Número de Publicaciones por Mes y Formato')
plt.ylabel('Cantidad')
plt.xlabel('Mes')
plt.legend(title='Formato')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 3. Likes totales por formato
plt.figure(figsize=(8, 5))
sns.barplot(data=df_likes, x='Formato', y='Likes', palette='pastel')
plt.title('Likes Totales por Formato')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 4. Engagement promedio por publicación
plt.figure(figsize=(8, 5))
sns.barplot(data=df_likes, x='Formato', y='Promedio_Likes_x_Publicación', palette='muted')
plt.title('Engagement: Promedio de Likes por Publicación')
plt.ylabel('Likes Promedio')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# ------------------ IMPRESIÓN DE ESTADÍSTICAS ---------------------
print("Total de publicaciones por formato:")
print(total_pub_format)
print("\nTotal de publicaciones por mes:")
print(df_pub[['Mes', 'Total_Publicaciones']])
print("\nResumen de Engagement:")
print(df_likes)
