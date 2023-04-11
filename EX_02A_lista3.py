from collections import deque

fila_pessoas = deque(['Maria', 'João', 'Pedro', 'Ana'])

def remove_pessoa():
    pessoa_removida = fila_pessoas.popleft()
    return pessoa_removida

#Teste
pessoa_removida = remove_pessoa()
print(pessoa_removida)