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
data['Nombre municipio'].replace('MEDELLiN', 'MEDELLIN', inplace=True)
data['Nombre municipio'].replace('Galapa', 'GALAPA', inplace=True)
data['Nombre municipio'].replace('barrancabermeja', 'BARRANCABERMEJA', inplace=True)
data['Nombre municipio'].replace('momil', 'MOMIL', inplace=True)
data['Nombre municipio'].replace('Anserma', 'ANSERMA', inplace=True)
data['Nombre municipio'].replace('Guepsa', 'GUEPSA', inplace=True)
data['Nombre municipio'].replace('Pensilvania', 'PENSILVANIA', inplace=True)
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
data['Nombre departamento'].replace('BARRANQUILLA', 'ATLANTICO', inplace=True)
data['Nombre departamento'].replace('BOGOTA', 'CUNDINAMARCA', inplace=True)
data['Nombre departamento'].replace('CARTAGENA', 'BOLIVAR', inplace=True)
data['Nombre departamento'].replace('STA MARTA D.E.', 'MAGDALENA', inplace=True)
data['Nombre departamento'].replace('Caldas', 'CALDAS', inplace=True)
data['Nombre departamento'].replace('Tolima', 'TOLIMA', inplace=True)
departamentos = data['Nombre departamento'].value_counts().shape[0]
print(f'El número de departamentos afectados son de: {departamentos}')

# 9. Liste los departamentos afectados(sin repetirlos)
lista_departamentos = data['Nombre departamento'].value_counts()
lista_departamentos

# 10. Ordene de mayor a menor por tipo de atención
tipo_atencion = data.sort_values('Ubicación del caso', ascending=False)
tipo_atencion.head()

# 11. Liste de mayor a menor los 10 departamentos con mas casos de contagiados
departamentos_m = lista_departamentos.sort_values(ascending=False).head(10)
departamentos_m

# 12. Liste de mayor a menor los 10 departamentos con mas casos de fallecidos
lista_fallecidos = data[data['Recuperado'] == 'Fallecido']
fallecidos_departamento = lista_fallecidos['Nombre departamento'].value_counts().head(10)
fallecidos_departamento

# 13. Liste de mayor a menor los 10 departamentos con mas casos de recuperados
lista_recuperados = data[data['Recuperado'] == 'Recuperado']
recuperados_departamento = lista_recuperados['Nombre departamento'].value_counts().head(10)
recuperados_departamento

# 14. Liste de mayor a menor los 10 municipios con mas casos de contagiados
lista_municipios = data['Nombre municipio'].value_counts()
lista_municipios.head(10)

# 15. Liste de mayor a menor los 10 municipios con mas casos de fallecidos
fallecidos_municipio = lista_fallecidos['Nombre municipio'].value_counts().head(10)
fallecidos_municipio

# 16. Liste de mayor a menor los 10 municipios con mas casos de recuperados
recuperados_municipio = lista_recuperados['Nombre municipio'].value_counts().head(10)
recuperados_municipio

# 17. Liste agrupado por departamento y en orden de Mayor a menor las ciudades
# con mas casos de contagiados
grupos_departamentos = data.groupby('Nombre departamento')
orden_ciudades = grupos_departamentos['Nombre municipio'].value_counts()
orden_ciudades

# 18. Número de Mujeres y hombres contagiados por ciudad por departamento
data.Sexo.replace('f', 'F', inplace=True)
data.Sexo.replace('m', 'M', inplace=True)
contagiados_h_m = (data.groupby(['Nombre departamento', 'Nombre municipio']))['Sexo'].value_counts()
contagiados_h_m
