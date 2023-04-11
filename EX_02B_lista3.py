from collections import deque

fila_numeros = deque([1,2,3])


def adiciona_numero(numero):
    fila_numeros.append(numero)


def remove_numero():
    numero_removido = fila_numeros.popleft()
    return numero_removido


# Teste
numero = input("Digite um número para ser adicionado: ")
numero_float = float(numero)
adiciona_numero(numero_float)
print(fila_numeros)

remove_numero()
print(fila_numeros)
remove_numero()
print(fila_numeros)



