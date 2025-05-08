"""
Análisis de concordancia entre jueces mediante el coeficiente W de Kendall.
Incluye corrección por empates, cálculo del estadístico chi-cuadrado,
y verificación de hipótesis con nivel de significancia ajustable.
"""
"""
Created on Wed May  7 20:43:29 2025

@author: Osmar de Jesús Pérez Lozada
"""
from collections import defaultdict
from scipy.stats import chi2


def ajustar_fila_coefT (lnumeros):
    """
        Calcula los rangos ligados ajustados para una lista de valores numéricos y 
        el coeficiente de corrección por empates (T= ∑(t³ - t)), útil para el cálculo 
        del coeficiente W de Kendall.
    
        Parámetros:
        ------------
        lnumeros : list of float or int
            Lista de calificaciones u observaciones asignadas por un juez a varios objetos.
    
        Retorna:
        --------
        list of float
            Lista de rangos ajustados (ligados), donde cada posición representa el rango 
            asignado al elemento original. El último valor de la lista es el coeficiente 
            de corrección por empates.
    
        Ejemplo:
        --------
        Entrada:  [10, 30, 30, 50, 70, 10]
        Salida:   [5.5, 3.5, 3.5, 2.0, 1.0, 5.5, 8]
        (6 rangos ajustados + coeficiente de corrección final)
    """
    
    def cum_mean(first, last):
        return (first + last) / 2
    
    #validar fila 
    
    for i, lvalor in enumerate(lnumeros):
        if not isinstance(lvalor, (int, float)):
            raise ValueError(f"Valor no numerico detectado en la fila, posicion {i+1} ")

    
    
    numeros=lnumeros.copy()
    numeros.sort(reverse=True)   # Ordena para asignar rangos descendentes
    
    # Diccionario para agrupar índices por valor
    posiciones = defaultdict(list)
    
    # Rellenar las posiciones
    vistos = []

    # Agrupa los valores iguales (empates) y conserva sus posiciones originales
    #guarda los items ordenados de mayor a menor 
    #agrupa los que se repiten
    #preservar el indicie de su posicion original
    for num in numeros:
        if not num in vistos:
           sublist = [lidx for lidx, lnum in enumerate(lnumeros) if num == lnum]
           posiciones[num].extend(sublist)
           vistos.append(num)

    
    lista = [0 for _ in range(len(lnumeros))] # Lista de salida con rangos ajustados
    acum=0  # Acumulador del coeficiente de corrección ∑(t³ - t)
    aux_i =len(lnumeros)     # indice del rango en el ciclo
    
    for idx  in posiciones:
        base = len(posiciones[idx]) # cantidad de items en el grupo
        item_coef = base**3-base    # coeficiente de guste para todos los items de ese grupo
        acum = acum  + item_coef    # guarda el acumulado para incluirlo al final de la fila
        media = cum_mean (aux_i-base+1, aux_i)
        for i in posiciones[idx]:  # completa la matriz de salida con rangos ajustados
            lista [i]=media  # asigna la media cada item del mismo grupo en su posicion original
            
        aux_i-=base
    
    lista.append(acum) # Añade el coeficiente de corrección al final
    return lista

def Kendall (matriz_aj, alpha=0.05):
    """
    Calcula el coeficiente W de Kendall a partir de una matriz de rangos ajustados con corrección por empates.
    Evalúa la concordancia entre múltiples jueces que clasifican un conjunto de objetos.

    Parámetros:
    -----------
    matriz_aj : list of list of float
        Matriz de tamaño k × (n+1), donde cada fila contiene:
        - n rangos ajustados asignados por un juez a n objetos.
        - el último valor de la fila es el coeficiente de corrección ∑(t³ - t) por empates de ese juez.
    
    alpha : float, opcional
        Nivel de significancia para la prueba de hipótesis. Valor por defecto: 0.05.

    Retorna:
    --------
      
        'W': W,                      # Coeficiente de concordancia de Kendall
        'K': K,                      # Estadístico chi-cuadrado calculado
        'gl': gl,                    # Grados de libertad (n - 1)
        'chi_critico': chi_critico,  # Valor crítico de chi-cuadrado para el nivel de significancia
        'p_valor': p_valor,          # P-valor asociado a K
        'concordancia': concordancia # Indicador logico de si existe concordancia significativa
    """
    
    kk   = len(matriz_aj)      # Número de jueces (filas)
    N   = len(matriz_aj[0])-1  # Número de objetos (columnas excluyendo el coeficiente)
    gl      = N-1              # Grados de libertad para chi-cuadrado
    
    # suma de cada columna
    filas_sum = []   
    # Calcular la suma de rangos por objeto (columna)
    filas_sum = [sum(fila[i] for fila in matriz_aj) for i in range(N)]
        
    #suma de cada columna al cuadrado 
    filas_sum_2 =  [i**2 for i in filas_sum] 
 
    # calculo de los coeficientes
    SDR = sum(filas_sum_2)-((sum(filas_sum)**2)/N)   # Varianza total corregida
    TCL = sum (fila[N] for fila  in matriz_aj)       # Suma total de correcciones por empates
    W = (12*SDR)/(((kk**2)*((N**3)-N))-kk*TCL)       # Cálculo del coeficiente W de Kendall (con corrección)
    K = W*kk*gl
    
    
    # Valor crítico de chi-cuadrado y p-valor
    chi_critico = chi2.ppf(1 - alpha, gl)
    p_valor = 1 - chi2.cdf(K, gl)
    concordancia = K > chi_critico
    

    return {
     'N': N, # cantdad de casos
    'W': W,                      # Coeficiente de concordancia de Kendall
    'K': K,                      # Estadístico chi-cuadrado calculado
    'gl': gl,                    # Grados de libertad (n - 1)
    'chi_critico': chi_critico,  # Valor crítico de chi-cuadrado para el nivel de significancia
    'p_valor': p_valor,          # P-valor asociado a K
    'concordancia': concordancia # Indicador booleano de si existe concordancia significativa
	}
