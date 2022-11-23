import logging
logging.basicConfig(level=logging.ERROR, filename="logs_example.log")

""" #1
import math

def number_validate(number):
      if number < 0:
            raise TypeError("O número deve ser maior que zero.")

def calc_raiz_quadrada():
      try:
            number = int(input('Digite um número para calcular sua raíz quadrada:'))
            number_validate(number)
            result = (math.isqrt(number))
            logging.info(result)
            print(f'O resultado da operação é {result}')
      except (ValueError, TypeError):
            print("Erro nos tipos de dados que você digitou")
            logging.error("Erro nos tipos de dados que você digitou")
      except KeyboardInterrupt:
            print("Dados não informados")
            logging.error("Dados não informados")
      finally:
            print("Operação finalizada")
            
calc_raiz_quadrada() """



#2
try:
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
    result = n1 / n2
    logging.info(result)
    print(f"O resultado da divisão dos dois números é: {result}")
except ZeroDivisionError:
    print("Não é possível dividir um número por zero")
    logging.error("Não é possível dividir um número por zero")
finally:
    print("Operação finalizada")
      
      