# main.py
# Ejemplo de uso del módulo kendall_w.py con datos embebidos

from kendall_w import ajustar_fila_coefT, Kendall

# Paso 1: Datos directamente en el script
data = [
    [7,9,8,8,6,9,7,8,5],
    [6,9,8,7,5,9,8,7,4],
    [5,9,8,7,6,8,9,7,4],
    [9,8,7,6,5,9,7,8,6],
    [6,9,8,7,6,8,8,9,5],
    [7,8,9,6,5,8,8,8,6],
    [6,5,8,6,4,8,9,9,7],
    [4,5,9,6,6,8,9,8,7],
    [7,5,8,5,6,8,8,9,6],
    [8,9,7,6,5,9,7,8,6],
    [9,8,7,6,5,8,9,7,5],
    [7,8,9,6,5,9,8,7,6],
    [5,7,8,9,6,8,7,9,8],
    [4,9,8,7,5,9,8,8,9],
    [6,8,9,7,5,8,8,9,7]
]

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
    print("[✔] Existe concordancia significativa entre jueces (rechazamos H₀)")
else:
    print("[✘] No se puede afirmar concordancia significativa (no se rechaza H₀)")