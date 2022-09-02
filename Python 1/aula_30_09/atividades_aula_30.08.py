""" variavel = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo']
print(type(variavel))

variavel_2 = (tuple(variavel))
print(variavel_2) """


#######################################################################


lista = ['banana', 'caju', 'melão', 5, 'pera', 10]

for index, elemento in enumerate(lista):
      if elemento == int:
            lista.pop()
            
print(index, elemento)