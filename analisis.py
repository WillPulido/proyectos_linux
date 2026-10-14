import requests
import pandas as pd

print("1. Descargando datos desde la API pública...")
url = "https://jsonplaceholder.typicode.com/posts"
respuesta = requests.get(url)
datos = respuesta.json()

print("2. Convirtiendo a tabla de datos (DataFrame de pandas)...")
df = pd.DataFrame(datos)

# Mostramos las primeras 5 filas para ver la estructura
print("\n--- Vista previa de los datos ---")
print(df.head())

# Creamos una columna nueva calculando la cantidad de caracteres de cada título
df["largo_titulo"] = df["title"].apply(len)

print("\n--- Resumen estadístico del largo de títulos ---")
print(df["largo_titulo"].describe())

# Agrupamos por usuario para ver cuántos registros tiene cada uno
print("\n--- Cantidad de publicaciones por usuario (primeros 5) ---")
conteo_usuarios = df["userId"].value_counts().head()
print(conteo_usuarios)
# --- BLOQUE DE TRANSFORMACIÓN Y EXPORTACIÓN ---
print("\n3. Filtrando y exportando datos relevantes...")

# Filtramos: publicaciones de los usuarios 1 y 2 con títulos de más de 40 caracteres
filtro = (df["userId"].isin([1, 2])) & (df["largo_titulo"] > 40)
df_filtrado = df[filtro][["userId", "id", "title", "largo_titulo"]]

print(f"Total de registros encontrados: {len(df_filtrado)}")
print(df_filtrado)

# Exportamos a un archivo CSV limpio
nombre_archivo = "reporte_usuarios.csv"
df_filtrado.to_csv(nombre_archivo, index=False, encoding="utf-8")

print(f"\n¡Éxito! Archivo guardado localmente como '{nombre_archivo}'.")
