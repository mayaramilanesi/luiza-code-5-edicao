'''
LISTAS

- Coleção ordenada de valores, onde cada valor é identificado por índices. Em Python representamos uma lista
separando os dados por vírgula, dentro de colchetes.
  Elas são utilizadas para armazenar diversos itens em uma única variável e existem várias maneiras de serem criadas.
  
  Ex: letters = ["a", "b", "c"]
                  0    1    2

- Podemos obter uma lista através de compreensão de listas (List Comprehensions)

Ex: [item for item iterável]

- Como acessar os dados de uma lista?

Ex:
      lista = ['Maçã', 'Banana', 'Jaca', 'Melão', 'Abacaxi']
      print(f'Estou buscando a fruta: {lista[2]}')
      output: Estou buscando a fruta: Jaca

- Para acessar o último dado de uma lista = [-1]

- Para saber o tamanho de uma lista = length

- Podemos acessar um item de uma lista dentro de outra lista utilizando os índices

- Para percorrer uma lista, deve-se usar loops

      Ex: lista = [0, 5, 8, 10, 35, 15, 7, 4, 12, 22, 3, 2, 9, 1]
      lista_numeros_maior_10 = []

      for i in lista:
            if i > 10:
                  lista_numeros_maior_10.append(i)
      
      print(f'Resultado da lista: {lista_numeros_maior_10}')
      
      
MÉTODOS PARA MANUSEAR UMA LISTA

- list.append(x) = adiciona um item ao fim da lista
- list.extend(iterable) = adiciona todos os itens do iterável ao fim da lista
- list.insert(i, x) = insere um item em uma dada possível (i) dada pelo index
- list.remove(x) = remove o primeiro elemento cujo o valor for 'x'
- list.pop(i) = remove o item da posição i da lista e retorna, caso o index não seja especificado, retorna o último elemento
- list.clear() = remove tudo da lista
- list.index(x[, start[, end]]) = retorna o indice do primeiro elemento cujo valor seja x
- list.count(x) = retorna o número de vezes que x aparece na lista
- list.sort(key=nome, reverse=False) = ordena os itens da lista
- list.reverse() = reverte os elementos da lista
- list.copy() = retorna uma lista com a cópia dos elementos da lista de origem

'''

