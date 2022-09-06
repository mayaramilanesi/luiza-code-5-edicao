def valor_comissao(valor_venda):
      comissao10 = float(valor_venda * 0.1)
      comissao20 = float(valor_venda * 0.2)
      comissao25 = float(valor_venda * 0.25)
      comissao30 = float(valor_venda * 0.3)
      
      if valor_venda < 1000:
            return 'Comissão = R$ 0,00'
      elif valor_venda >= 1000 and valor_venda < 5000:
            return f'Comissão = R$ {comissao10}'
      elif valor_venda >= 5000 and valor_venda < 10000:
            return f'Comissão = R$ {comissao20}'
      elif valor_venda >= 10000 and valor_venda < 50000:
            return f'Comissão = R$ {comissao25}'
      elif valor_venda >= 50000:
            return f'Comissão = R$ {comissao30}'
      
print(valor_comissao(35000))
      