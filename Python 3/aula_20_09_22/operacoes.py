import logging

logging.basicConfig(level=logging.ERROR, filename="logs_example.log")

try:
    numerator = int(input("Numerador: "))
    denominator = int(input("Denominador: "))
    result = numerator / denominator
    logging.info(result)
    print(f"O resultado é {result}")
except ZeroDivisionError:
    print("Não é possível dividir um número por zero")
    logging.error("Não é possível dividir um número por zero")
except (ValueError, TypeError):
    print("Erro nos tipos de dados que você digitou")
except KeyboardInterrupt:
    print("Dados não informados")
finally:
    print("Obrigada!")