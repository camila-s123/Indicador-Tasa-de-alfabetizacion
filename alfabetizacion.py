#Shirley Guanochanga
#Karol Loachamin
#Juan Morales
#Kerly Salazar
#Camila Silva
# **Actividad "Análisis de indicadores del Banco Mundial"**

# Este será mi script para visualización
import pandas as pd
import numpy as np
import matplotlib.pyplot  as plt
import seaborn as sns

#PREGUNTA 1
#Exportar los datos del indicador Tasa de alfabetización en adultos 
df_countries_alfabetizacion = pd.read_excel('API_SE.ADT.LITR.ZS_DS2_es_excel_v2_6307788.xls',sheet_name = "Metadata - Countries")


# Filtrar el dataframe paises america latina:
paises_America_Latina = df_countries_alfabetizacion[df_countries_alfabetizacion["Region"] == "América Latina y el Caribe (excluido altos ingresos)"]["Country Name"].unique()


#filtrar por el año 
df_anios = pd.read_excel("API_SE.ADT.LITR.ZS_DS2_es_excel_v2_6307788.xls",sheet_name="Data",skiprows=  3)
df_anios_filtrado = df_anios[df_anios['Country Name'].isin(paises_America_Latina)]
df_anio_2020 = df_anios_filtrado[["Country Name","2020"]]


#imprimir información resultante
print("Paises filtrados:", paises_America_Latina)
print(df_anios_filtrado)
print(df_anio_2020)


# **Indicadores de America Latina**


## Calcular el valor promedio del indicador seleccionado
indicador_seleccionado = 'Tasa de alfabetización de adultos'
valor_promedio = df_anio_2020["2020"].mean()


# Mostrar el resultado (Interpretación)
print(f"El valor promedio del indicador de la '{indicador_seleccionado}' en América Latina y el Caribe (excluido altos ingresos) en el año 2020 es: {valor_promedio}")


#PREGUNTA 2
# Filtrar datos para países de América Latina
df_anios = pd.read_excel("API_SE.ADT.LITR.ZS_DS2_es_excel_v2_6307788.xls",sheet_name="Data",skiprows=  3)
df_anios_filtrado = df_anios[df_anios['Country Name'].isin(paises_America_Latina)]


#Visualización de los datos filtrados
df_anios_filtrado


#Señalamos las columnas mas importantes 
columnas_relevantes = ['Country Name', 'Country Code', 'Indicator Code'] + list(df_anios_filtrado.columns[4:])
df_anios_filtrado = df_anios_filtrado[columnas_relevantes]


# Transponer el DataFrame para facilitar el trazado
df_anios_transpuesto = df_anios_filtrado.set_index(['Country Name', 'Country Code', 'Indicator Code']).transpose()


# Creación de la gráfica
plt.figure(figsize=(12, 6))

# Graficar datos para cada país
for pais in paises_America_Latina:
    plt.plot(df_anios_transpuesto.index, df_anios_transpuesto.xs(key=(pais, 'SE.ADT.LITR.ZS'), axis=1, level=[0, 2]).astype(float), label=pais)
    
# Establecer límites de los ejes x e y después de trazar los datos
plt.ylim(70, 100)


# Configurar título y etiquetas de ejes
plt.title('Evolución de la Tasa de Alfabetización en América Latina')
plt.xlabel('Año')
plt.ylabel('Tasa de Alfabetización')
plt.legend()
plt.xticks(rotation=55)
plt.grid(True)
plt.show()


#PREGUNTA 3
# Seleccionar las columnas de los últimos 5 años
columnas_ultimos_anios = df_anios_filtrado.columns[-5:]

# Filtrar el DataFrame para incluir solo las columnas de los últimos 5 años
df_ultimos_anios = df_anios_filtrado[['Country Name', 'Country Code', 'Indicator Code'] + list(columnas_ultimos_anios)]

# Convertir las columnas a tipo numérico
df_ultimos_anios = df_ultimos_anios.apply(pd.to_numeric, errors='coerce')


# Calcular la matriz de correlación
matriz_correlacion_ultimos_anios = df_ultimos_anios.corr()

matriz_correlacion_ultimos_anios = matriz_correlacion_ultimos_anios.iloc[3:, 3:]


# Configurar el tamaño de la figura
plt.figure(figsize=(12, 8))

# Crear el mapa de calor con Seaborn
sns.heatmap(matriz_correlacion_ultimos_anios, annot=True, cmap="coolwarm", fmt=".2f", linewidths=.5)

# Añadir etiquetas y título
plt.title('Mapa de Correlación - Últimos 5 años para América Latina')
plt.xlabel('Variables')
plt.ylabel('Variables')

# Mostrar el mapa de correlación
plt.show()









