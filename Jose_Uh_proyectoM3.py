import numpy as np
import matplotlib.pyplot as plt

def calcular_canicas(canicas, niveles):
    '''
    Simula el proceso de caída de canicas en una máquina de Galton.
    Parámetros:
    - canicas: el número de canicas que caen.
    - niveles: el número de niveles en la máquina de Galton.

    Retorna:
    - posiciones: el conteo de canicas en cada posición final después de la simulación.

    '''
    posiciones = np.zeros(niveles)                  # Cuenta el numero de canicas en cada posición final         
    for _ in range(canicas):                        # Realiza la simulación para cada canica
        posicion = 0
        for _ in range(niveles - 1):                # Simula el movimiento de la canica en cada nivel
            direccion = np.random.randint(0, 2)     # # Escoge aleatoriamente la dirección (izquierda o derecha)
            if direccion == 1:
                posicion += 1
        posiciones[posicion] += 1                   # Incrementa el contador de canicas en la posición final
    return posiciones


def graficar_histograma(posiciones):
    '''
    Grafica un histograma de los datos obtenidos.

    '''
    plt.bar(range(len(posiciones)), posiciones, color='#FF0000', alpha=0.6)     # Crea un histograma con barras rojas semi-transparente
    plt.xlabel('Posicion')                                                      # Nombre del eje X
    plt.ylabel('Numero de canicas')                                             # Nombre del eje Y
    plt.title('Histograma de la Máquina de Galton', fontsize=14, fontweight='bold')         # Título del gráfico
    plt.grid(axis='y', linestyle='--', alpha=0.7)                               # Agrega una cuadrícula punteada en el eje y
    plt.show()

    

if __name__ == "__main__":
    # Parámetros de la simulación
    canicas = 3000                                  # Número de canicas que caen
    niveles = 12                                    # Número de niveles en la máquina de Galton

    # Realiza la simulación y grafica los posiciones
    resultados = calcular_canicas(canicas, niveles)
    graficar_histograma(resultados)