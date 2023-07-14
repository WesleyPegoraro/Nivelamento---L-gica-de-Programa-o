# LISTAS EM PYTHON
# - O conteúdo dos elementos é heterogêneo
# - Os elementos são dinâmicos, ou seja, acrescentamos ou excluímos quando quisermos
# - O append acrescenta um item no final. lista.append(45)
# - O insert permite editar um elemento. lista.insert(indice, conteudo)
# - O pop remove o último elemento da lista. lista.pop()
# - O clear apaga todos os elementos da lista. lista.clear

## listas em Python pode ter elementos heterogeneos
lista = ["a", 2, True, 4.5]
print(lista)

## adicionando um elemento no final da lista
lista.append(45)
print(lista)

## editando um elemento existente
lista.insert(0, 56)
print(lista)

## pop remove o últmo elemento
lista.pop()
print(lista)

## apaga todos os elementos da lista
lista.clear()
print(lista)

## preenchendo os 5 elementos da lista - FORMA 1
lista = []
for cont in range(0, 5, 1):
    x = float(input("Digite um elemento: "))
    lista.append(x)
print(lista)

## exibindo os 5 elementos da lista - FORMA 1
for i in range(0, 5, 1):
    print(lista[i])

## exibindo os 5 elementos da lista - FORMA 2
for elem in lista:
    print(elem)

## somando os elementos da lista
soma = 0
for elem in lista:
    soma += elem # soma = soma + elem
print(soma)