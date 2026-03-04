numeros = [10, 5, 8, 20, 3, 15]

def pares(numeros):
    pares_lista = []
    
    for i in numeros:
        if i % 2 == 0:
            pares_lista.append(i)
    
    return pares_lista

print(pares(numeros))