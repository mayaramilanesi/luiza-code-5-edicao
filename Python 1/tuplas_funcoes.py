'''
TUPLAS

- É uma estrutura imutável
- São utilizadas para adicionar tipos diferentes de informações em uma mesma variável
- Garante segurança nas informações armazenadas



map() - Sintax map(função, iteráveis)
- Realiza uma operação específica nos itens da lista e transforma-os em outra coisa

Ex:
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_somada = map( lambda x: x+x, lista)
print(list(lista_somada))



filter() - Sintax filter(função, iteráveis)
- Utilizado quando precisamos filtrar elementos da lista

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = filter( lambda x: x%2, lista)
print(list(pares))



reduce() - Sintax reduce(função, iteráveis)
- Aplica uma operação em todos os elementos da lista reduzindo a apenas um elemento. Precisamos importar o módulo functools.

from functools import reduce

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
soma = reduce( lambda x, y: x+y, lista, 0)
print(soma)



FUNÇÕES (nome, parâmetros e corpo)
- Sequência de linhas que representa algum comportamento
- Uma função só é executada quando chamamos por ela

Ex:
def foo(value):
      print(f'Olá, esse é o parâmetro: {value}')
      
foo('LuizaCode')

'''

