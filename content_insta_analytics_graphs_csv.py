'''
MES ---   POST --- STORY --- REEL --- LIVE
-------------------------------------------------------
ENERO      1        15        0        1
FEBRERO    0         0        0        0
MARZO      9        40        4        1
ABRIL     15        54        8        0 
MAYO      11        27        5        0
JUNIO     
'''

'''cruzar con las visualizaciones de las story y los me gusta de los post y reel'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = { 
    'Mes': ['Post', 'Story', 'Reel', 'Live'],
    'Enero': [],
    'Febrero': [],
    'Marzo': [],
    'Abril': [],
    'Mayo': [],
    'Junio': []
}

df = pd.DataFrame(data)  # Convierte los datos en una tabla para manejarlos fácilmente