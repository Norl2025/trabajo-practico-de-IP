from typing import Any
from biblioteca import sonBarcosVálidos, BarcoEnGrilla, tamañoBarco

## Ejercicio 1

def cantidadDeBarcosDeTamaño(barcos: list[BarcoEnGrilla], tamaño: int) -> int:
    """ Agregar docstring acá
    """
    res: int = 0
    for barco in barcos:
        if tamañoBarco(barco) == tamaño:
            res += 1
        else: 
            res += 0
    return res # TODO: Implementame

# Ejercicio 2

def nuevoJuego(
        cantidadDeFilas: int,
        cantidadDeColumnas: int,
        barcosDisponibles: list[Barco]
    ) -> EstadoJuego:
    """ Agregar docstring acá
    """
    # TODO: Implementame
    return((5,5), [3, 3, 2], [UNO],
            ([[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),
            ([[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]])
    )

# ## Ejercicio 3

# def esEstadoDeJuegoVálido(estadoDeJuego: EstadoJuego) -> bool:
#     """ Agregar docstring acá
#     """
#     return False # TODO: Implementame


# ## Ejercicio 4

# def dispararEnPosición(estado_juego: EstadoJuego, posición: Posición) -> ResultadoDisparo:
#     """ Agregar docstring acá
#     """
#     return NADA # TODO: Implementame


# ## Ejercicio 5

# def barcosEnGrilla(grilla: Grilla) -> list[BarcoEnGrilla]:
#     """ Agregar docstring acá
#     """
#     return [] # TODO: Implementame



