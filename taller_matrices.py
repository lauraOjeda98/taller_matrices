# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 13:22:55 2021

@author: laura
"""

import pandas as pd

url = '../covid_22_noviembre.csv'
data = pd.read_csv(url)

# 1. Número de casos de Contagiados en el País
casos = data.shape[0]
print(f'El número de casos de contagios en el país es de: {casos}')

# 2. Número de Municipios Afectados
municipios = data['Nombre municipio'].value_counts().shape[0]
print(f'El número de municipios afectados es de: {municipios}')
