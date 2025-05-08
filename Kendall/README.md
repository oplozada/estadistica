**Título: Implementación personalizada del coeficiente W de Kendall con
corrección por empates**

**1. Descripción general**

Este proyecto implementa el cálculo del coeficiente de concordancia W de
Kendall para evaluar la consistencia entre múltiples jueces al
clasificar un conjunto de objetos. La implementación incluye corrección
por empates y cálculo del estadístico chi-cuadrado para pruebas de
hipótesis.

**2. ¿Qué hace el código?**

1.  Ajusta rangos con corrección por empates mediante rangos
    promediados.

2.  Calcula el coeficiente \$W\$ de Kendall.

3.  Obtiene el estadístico de contraste \$K\$ (chi-cuadrado).

4.  Evalúa significancia estadística mediante p-valor y valor crítico.

5.  Compatible con entrada desde archivos .csv.

**3. Validación**

1.  Los resultados han sido **contrastados con la salida de SPSS**
    utilizando los mismos conjuntos de datos.

2.  La concordancia entre resultados es exacta hasta cuatro cifras
    decimales.

3.  También se comparó con fórmulas en manuales clásicos de estadística
    no paramétrica (por ejemplo, Siegel y Castellan).

**4. Archivos incluidos**

1.  kendall_w.py: módulo principal con las funciones ajustar_fila_coefT() y
    Kendall().

2.  main.py: script de ejemplo para uso práctico.

3.  datos_jueces.csv: archivo con los datos de entrada.

4.  README.md o este documento: explicación del funcionamiento y
    validación.



6.  **Ejemplo de salida de datos**

> Cantidad de casos : 9
> Grados de Libertad : 8
> W de Kendall: 0.8049
> Chi-cuadrado calculado (K): 70.8289
> Chi-cuadrado crí­tico (α = 0.01): 20.0902
> P-valor: 0.00000000000336
> \[ok\] Existe concordancia significativa entre jueces (rechazamos Ho)
