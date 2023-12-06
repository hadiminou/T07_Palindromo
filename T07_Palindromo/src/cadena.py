def es_palindromo(cadena:str)->bool:
    longitud=len(cadena)
    res=True
    for posicion in range(0,longitud//2):
        if cadena[posicion]!=cadena[-1-posicion]:
            res=False
            break
    return res