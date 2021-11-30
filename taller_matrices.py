# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 13:22:55 2021

@author: laura
"""

import pandas as pd
import matplotlib.pyplot as plt

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
data['Ubicación del caso'].replace('Casa', 'CASA', inplace=True)
data['Ubicación del caso'].replace('casa', 'CASA', inplace=True)
tipo_atencion = data['Ubicación del caso'].value_counts()
tipo_atencion

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

# 19. Liste el promedio de edad de contagiados por hombre y mujeres por
# ciudad por departamento
promedio_edades = data.groupby(['Nombre departamento', 'Nombre municipio', 'Sexo'])['Edad'].mean()
promedio_edades

# 20. Liste de mayor a menor el número de contagiados por país de procedencia
data['Nombre del país'].replace('MEXICO', 'MÉXICO', inplace=True)
data['Nombre del país'].replace('VENEUELA', 'VENEZUELA', inplace=True)
data['Nombre del país'].replace('ARABIA SAUDÍ', 'ARABIA SAUDITA', inplace=True)
data['Nombre del país'].replace('REPÚBLICA DOCIMINCANA', 'REPÚBLICA DOMINICANA', inplace=True)
contagios_pais = data['Nombre del país'].value_counts()
contagios_pais

# 21. Liste de mayor a menor las fechas donde se presentaron mas contagios
fecha_contagios = data['Fecha de inicio de síntomas'].value_counts()
fecha_contagios

# 22. Diga cual es la tasa de mortalidad y recuperación que tiene toda Colombia
tasa_mortalidad = (lista_fallecidos.shape[0]/data.shape[0])*100
tasa_recuperados = (lista_recuperados.shape[0]/data.shape[0])*100
print(f'La tasa de mortalidad en Colombia es de: {tasa_mortalidad}')
print(f'La tasa de recuperados en Colombia es de: {tasa_recuperados}')

# 23. Liste la tasa de mortalidad y recuperación que tiene cada departamento
mortalidad_dep = lista_fallecidos['Nombre departamento'].value_counts()
tasa_mortalidad = (mortalidad_dep.divide(lista_departamentos, fill_value=0)).multiply(100)
tasa_mortalidad

recuperados_dep = lista_recuperados['Nombre departamento'].value_counts()
tasa_recuperados = (recuperados_dep.divide(lista_departamentos, fill_value=0)).multiply(100)
tasa_recuperados

# 24. Liste la tasa de mortalidad y recuperación que tiene cada ciudad
mortalidad_mun = lista_fallecidos['Nombre municipio'].value_counts()
tasa_mortalidad_mun = (mortalidad_mun.divide(lista_municipios, fill_value=0)).multiply(100)
tasa_mortalidad_mun

recuperados_mun = lista_recuperados['Nombre municipio'].value_counts()
tasa_recuperados_mun = (recuperados_mun.divide(lista_municipios, fill_value=0)).multiply(100)
tasa_recuperados_mun

# 25. Liste por cada ciudad la cantidad de personas por atención
personas_atencion = (data.groupby('Nombre municipio'))['Ubicación del caso'].value_counts()
personas_atencion

# 26. Liste el promedio de edad por sexo por cada ciudad de contagiados
promedio_edad_mun = data.groupby(['Nombre municipio', 'Sexo'])['Edad'].mean()
promedio_edad_mun

# 27. Grafique las curvas de contagio, muerte y recuperación de toda Colombia acumulados
data['fecha reporte web'] = pd.to_datetime(data['fecha reporte web'])
data['Fecha de inicio de síntomas'] = pd.to_datetime(data['Fecha de inicio de síntomas'])
data['Fecha de muerte'] = pd.to_datetime(data['Fecha de muerte'])
data['Fecha de recuperación'] = pd.to_datetime(data['Fecha de recuperación'])
data['Fecha de diagnóstico'] = pd.to_datetime(data['Fecha de diagnóstico'])

print('Gráfica de contagio: ')
data.groupby('Fecha de inicio de síntomas').size().cumsum().plot()
print('Gráfica de recuperación: ')
data.groupby('Fecha de recuperación').size().cumsum().plot()
print('Gráfica de muertes: ')
data.groupby('Fecha de muerte').size().cumsum().plot()

# 28. Grafique las curvas de contagio, muerte y recuperación de los 10
# departamentos con mas casos de contagiados acumulados

# Contagio
leg = []
for i in range(10):
    leg.append(str(departamentos_m.index[i]))

for x in range(10):
    aux = data[data['Nombre departamento'] == str(departamentos_m.index[x])]
    aux.groupby('Fecha de inicio de síntomas').size().cumsum().plot().legend(leg)

# Muerte
for x in range(10):
    aux = data[data['Nombre departamento'] == str(departamentos_m.index[x])]
    aux.groupby('Fecha de muerte').size().cumsum().plot().legend(leg)

# Recuperados
for x in range(10):
    aux = data[data['Nombre departamento'] == str(departamentos_m.index[x])]
    aux.groupby('Fecha de recuperación').size().cumsum().plot().legend(leg)

# 29. Grafique las curvas de contagio, muerte y recuperación de las 10
# ciudades con mas casos de contagiados acumulados
municipios_m = lista_municipios.head(10)

leg2 = []
for i in range(10):
    leg2.append(str(municipios_m.index[i]))

for x in range(10):
    aux = data[data['Nombre municipio'] == str(municipios_m.index[x])]
    aux.groupby('Fecha de inicio de síntomas').size().cumsum().plot().legend(leg2)

# Muerte
for x in range(10):
    aux = data[data['Nombre municipio'] == str(municipios_m.index[x])]
    aux.groupby('Fecha de muerte').size().cumsum().plot().legend(leg2)

# Recuperados
for x in range(10):
    aux = data[data['Nombre municipio'] == str(municipios_m.index[x])]
    aux.groupby('Fecha de recuperación').size().cumsum().plot().legend(leg2)

# 30. Liste de mayor a menor la cantidad de fallecidos por edad en toda
# Colombia.
fallecidos_edad = lista_fallecidos['Edad'].value_counts()
fallecidos_edad

# 31. Liste el porcentaje de personas por atención de toda Colombia
total = data.shape[0]
porcentaje = (tipo_atencion.divide(total)).multiply(100)
porcentaje
