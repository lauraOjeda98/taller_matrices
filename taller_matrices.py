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

# 3. Liste los municipios afectados (sin repetirlos)
data['Nombre municipio'].replace('puerto COLOMBIA', 'PUERTO COLOMBIA', inplace=True)
data['Nombre municipio'].replace('puerto colombia', 'PUERTO COLOMBIA', inplace=True)
data['Nombre municipio'].replace('ALBAN (SAN JOSE)', 'ALBAN', inplace=True)
mun_afectados = data.groupby('Nombre municipio').size().shape[0]
print(f'El número de municipios afectados es de: {mun_afectados}')

# 4. Número de personas que se encuentran en atención en casa
casa = data[data['Ubicación del caso'] == 'Casa'].shape[0]
print(f'El número de personas que tiene atención en casa es de: {casa}')

# 5. Número de personas que se encuentran recuperados
recuperado = data[data['Recuperado'] == 'Recuperado'].shape[0]
print(f'El número de personas recuperadas es de: {recuperado}')

# 6. Número de personas que ha fallecido
fallecidos = data[data['Recuperado'] == 'Fallecido'].shape[0]
print(f'El número de personas fallecidas es de: {fallecidos}')

# 7. Ordenar de Mayor a menor por tipo de caso (Importado, en estudio,
# Relacionado)
importado = data[data['Tipo de contagio'] == 'Importado'].sort_values('Tipo de contagio', ascending=False)
estudio = data[data['Tipo de contagio'] == 'En estudio'].sort_values('Tipo de contagio', ascending=False)
relacionado = data[data['Tipo de contagio'] == 'Relacionado'].sort_values('Tipo de contagio', ascending=False)

# Número de departamentos afectados
departamentos = data['Nombre departamento'].value_counts().shape[0]
print(f'El número de departamentos afectados son de: {departamentos}')
