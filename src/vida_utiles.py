import random

def crear_tablero(filas: int, columnas: int) -> list[list[bool]]:
    """
    Crea un nuevo tablero vacío, con todas las células muertas.
    Parametros:
        filas (int): Número de filas del tablero.
        columnas (int): Número de columnas del tablero.
    Devuelve:
        Una lista de listas con todos los elementos False.
    """
    # TODO: Ejercicio 1
    '''
    Implementa la función crear_tablero que recibe el número de filas y de columnas y devuelve un nuevo tablero con todas las celdas iguales a False. 
    El tablero se representa mediante una lista de filas, siendo cada fila una lista de celdas (una por columna). 
    Por ejemplo, crear_tablero(2, 3) devolvería [[False, False, False], [False, False, False]]
    '''
    tablero=[]
    for i in range (filas):
        tablero.append([False]*columnas)
    return tablero 

def crear_tablero_aleatorio(filas: int, columnas: int, probabilidad_vida: float) -> list[list[bool]]:
    """
    Crea un tablero con células vivas distribuidas aleatoriamente.

    Parámetros:
        filas (int): Número de filas del tablero.
        columnas (int): Número de columnas del tablero.
        probabilidad_vida (float): Un valor entre 0.0 y 1.0 que representa la
                                   probabilidad de que una célula esté viva.

    Devuelve:
        Una lista de listas que representa el tablero con células vivas (True) y muertas (False).
    """
    # TODO: Ejercicio 2
    '''
    Para decidir si una celda está viva o muerta, puedes utilizar la función random.random(), que devuelve un valor aleatorio entre 0 y 1:

        Si random.random() < probabilidad_vida, la celda estará viva.
        Si no, estará muerta.
        Consejo: puedes comenzar creando un tablero vacío del tamaño adecuado, llamando a la función crear_tablero.
    '''
    tablero=crear_tablero(filas,columnas)
    for i in range (filas):
        for j in range (columnas):
            if random.random() < probabilidad_vida:
                tablero[i][j]=True
    return tablero 


def insertar_patron(tablero: list[list[bool]], patron: list[list[bool]], pos_fila: int, pos_col: int):
    """
    Inserta un patrón (una pequeña matriz) en el tablero en una posición dada.
    Parámetros:
        tablero (list[list[bool]]): El tablero donde se insertará el patrón.
        patron (list[list[bool]]): El patrón a insertar.
        pos_fila (int): La fila en la que se insertará la esquina superior izquierda del patrón.
        pos_col (int): La columna en la que se insertará la esquina superior izquierda del patrón.
    """
    # TODO: Ejercicio 3
    '''
    El patrón es una matriz de booleanos (lista de listas), igual que tablero, pero más pequeña. La función debe escribir los valores del patrón en el tablero, 
    empezando en la posición indicada.

    Puedes usar el siguiente algoritmo:

        Recorrer los índices de fila del patrón
        Para cada índice de fila, recorrer los índices de columna del patrón
        Asignar la posición actual del patrón a la posición del tablero resultante de sumar la posición actual a la posición recibida por parámetros.
        ¡Atención!: debes tener cuidado de no escribir fuera del tablero. Si un patrón no cabe en el sitio indicado, simplemente no escribimos las celdas que se salgan.
    '''
    columnas_tablero=len(tablero) #largo son las columnas
    if columnas_tablero>0:
        filas_tablero=len(tablero[0]) #ancho son las filas
    else:
        filas_tablero=0
    
    if pos_fila<filas_tablero and pos_col<columnas_tablero:
        columnas_patron=len(patron)
        if columnas_patron>0:
            filas_patron=len(patron[0])
        if pos_fila+filas_patron > filas_tablero-pos_fila:
            fila_borde=filas_tablero-pos_fila
        else:
            fila_borde=pos_fila+filas_patron
        if pos_col+columnas_patron > columnas_tablero-pos_col:
            col_borde=columnas_tablero-pos_col
        else:
            col_borde=pos_col+columnas_patron

        for i in range(pos_fila,fila_borde):
            for j in range(pos_col,col_borde):
                tablero[i][j]=patron[i-pos_fila][j-pos_col]

    


def contar_vecinos(tablero: list[list[bool]], fila: int, col: int) -> int:
    """
    Cuenta el número de vecinos vivos de una célula en la posición (fila, col).
    El tablero es toroidal, lo que significa que los bordes se conectan.
    Parámetros:
        tablero (list[list[bool]]): El tablero actual.
        fila (int): La fila de la célula.
        col (int): La columna de la célula.
    Devuelve:
        El número de vecinos vivos (int).
    """
    # TODO: Ejercicio 4
    '''
    Puedes usar el siguiente algoritmo:
        Iterar un índice i para los valores -1, 0 y 1.
        Iterar un índice j para los valores -1, 0, 1.
        Utilizar los índices anteriores y la posición de la celda para la que estamos contando los vecinos, para acceder a cada posición vecina. 
        Ten en cuenta que no debemos contar la propia celda para la que estamos haciendo el cálculo.
        ¡Atención!: Vamos a implementar un tablero toroidal. Esto significa que si nos salimos del tablero por la derecha, apareceríamos por la izquierda, y que si nos salimos por abajo, 
        apareceríamos por arriba. Ten en cuenta esto al escribir la expresión para acceder a las celdas vecinas.
    '''
    cuantos=0
    columnas_tablero=len(tablero) #largo son las columnas
    if columnas_tablero>0:
        filas_tablero=len(tablero[0]) #ancho son las filas
    
        for i in (-1,0,1):
            for j in (-1,0,1):
                if j !=0 and i!=0:
                    if tablero[(fila+i) % filas_tablero][(col+j) % columnas_tablero]==True:
                        cuantos+=1
    return cuantos



def calcular_siguiente_generacion(tablero):
    """
    Calcula el estado del tablero en el siguiente paso de tiempo basándose en las reglas
    del Juego de la Vida.
    Parámetros:
        tablero (list[list[bool]]): El tablero actual.
    Devuelve:
        Una nueva lista de listas que representa el tablero en la siguiente generación.
    """
    # TODO: Ejercicio 5
    pass
