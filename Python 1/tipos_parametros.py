# PARÂMETROS

# - Nomes dados aos atributos que uma função pode receber, definem quais são os argumentos aceitos por uma função, podendo ou não ter um valor padrão.

# Ex:

def calcula_salario(valor, horas=220):
      return valor * horas

print(calcula_salario(35))


# *args 

# - São apenas usados por convenção
# - *args é usado para passar uma lista de argumentos variável sem palavras chave em forma de tupla, 
#    pois a função que recebe não necessariamente saberá quantos argumentos serão passados.
# Ex:

def foo(*args):
      print(f'conteudo: {args}')
      
      for i in args:
            print(i)
            
foo('Hello', 'Moças', 'LuizaCode')

# **kwargs
# - É a abreviação de keyword arguments, ele permite passar um dicionário com inúmeras chaves para a função
#   Isso deixa definido que tal função irá receber tais valores.
# Ex:

def fooo(**kwargs):
      print(f'O nome dela(e) é: {kwargs.get("nome")}')
      
fooo(nome='Jhon',
    idade='28',
    pais='Brasil')


# DECORATOR
# - Usando o decorator, conseguimos adicionar qualquer comportamento antes e depois da execução de uma função qualquer



#LAMBDA

# sintaxe: lambda argument(s): expression
# - Boa para operações lógicas simples e funções que serão usadas apenas uma vez
# - Só podem executar uma única expressão, não pode ter mais que uma linha
# Ex:

lista = [1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x: x%2==0, lista)))