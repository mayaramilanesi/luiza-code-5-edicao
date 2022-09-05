
#preço total do carrinho


def soma_valor_total_carrinho(sacola):
      soma_total = 0
      for s in sacola:
            soma_total = soma_total + ( s[3] * s[2] )
            
      return soma_total

def cria_sacola():
      item1 = ['123', '1', 800.00, 1]
      item2 = ['456', '1', 40.00, 2]

      sacola = [item1, item2]
      
      valor = soma_valor_total_carrinho(sacola)

      print(valor)
      
cria_sacola()

