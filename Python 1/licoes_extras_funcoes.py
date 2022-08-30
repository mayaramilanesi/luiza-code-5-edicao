'''
Entrada:

lista = [100, 248.90, 88, 124.90]

def desconto(preco):
      return preco*(1-0.1)
      
1 - Dada uma lista com n valores, aplicar a função de desconto usando map()
2 - Retornar os valores maiores que 100, usando filter()
3 - Somar todos os valores da lista usando reduce()


Saída:
1 - [90.0, 224.01000000000002, 79.2, 112.41000000000001]
2 - [248.9, 124.9]
3 - 561.8

'''


lista = [100, 248.90, 88, 124.90]

def desconto(preco):
      return preco*(1-0.1)

#MAP

descontos = map(desconto, lista)
print(list(descontos))


#Filter

maiores_100 = filter(lambda x: x > 100, lista)
print(list(maiores_100))


#Reduce

from functools import reduce

soma_lista = reduce(lambda x, y: x+y, lista)
print(soma_lista)
