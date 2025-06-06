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

'''cruzar con las visualizaciones de las story y los me gusta de los post y reel'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = { 
    'Mes': ['Seguidores'],
    'Enero': [],
    'Febrero': [],
    'Marzo': [],
    'Abril': [],
    'Mayo': [],
    'Junio': []
}

df = pd.DataFrame(data)  # Convierte los datos en una tabla para manejarlos fácilmente