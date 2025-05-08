# main.py
# Ejemplo de uso del mÃ³dulo kendall_w.py con datos cargados desde un archivo CSV

import pandas as pd
from kendall_w import ajustar_fila_coefT, Kendall

# Paso 1: Cargar datos desde archivo CSV
# Cada fila representa un juez, cada columna un objeto evaluado
archivo_csv = "datos_jueces_2.csv"
#archivo_csv = "kendall.csv"
df = pd.read_csv(archivo_csv, header=None,sep=',')
data = df.values.tolist()

# Paso 2: Ajustar los rangos y calcular correcciones
matriz_ajustada = [ajustar_fila_coefT(fila) for fila in data]

# Paso 3: Calcular Kendall W
resultados = Kendall(matriz_ajustada, alpha=0.01)

# Paso 4: Mostrar resultados
print(f"Cantidad de casos : {resultados['N']:.0f}")
print(f"Grados de Libertad : {resultados['gl']:.0f}")
print(f"W de Kendall: {resultados['W']:.4f}")
print(f"Chi-cuadrado calculado (K): {resultados['K']:.4f}")
print(f"Chi-cuadrado crí­tico (α  = 0.01): {resultados['chi_critico']:.4f}")
print(f"P-valor: {resultados['p_valor']:.14f}")

if resultados['concordancia']:
    print("[ok] Existe concordancia significativa entre jueces (rechazamos Ho)")
else:
    print("[x] No se puede afirmar concordancia significativa (no se rechaza Ho)")
