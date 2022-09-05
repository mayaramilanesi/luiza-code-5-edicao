

'''______________CLASSES_____________________'''



'''______________ABSTRAÇÃO_____________________

class CampeonatoCrossfit:
          
      def __init__(self, tempo_time1, tempo_time2, tempo_time3, tempo_time4):
            self.tempo_time1 = tempo_time1
            self.tempo_time2 = tempo_time2
            self.tempo_time3 = tempo_time3
            self.tempo_time4 = tempo_time4
            
      def calcula_campeao(self):
            tabela_classificacao = [self.tempo_time1, self.tempo_time2, self.tempo_time3, self.tempo_time4]
            
            for i in tabela_classificacao:
                  if i <= 2:
                        print(f'Classificado')
                  else:
                        print('Desclassificado')
                        
tempo_times = CampeonatoCrossfit(1, 2, 3, 4)
tempo_times.calcula_campeao()'''






'''______________ENCAPSULAMENTO_____________________


class CalculaConta:
      def __init__(self, cpf, saldo_inicial, entrada, saída):
            self.__cpf__ = cpf
            self.__saldo_inicial__ = saldo_inicial
            self.__entrada__ = entrada
            self.__saida__ = saída
            
      def validar_usuario(self):
            if self.__cpf__ <= 99999999999:
                  print('Usuário verificado')
            else:
                  print('Usuário não verificado')
                  
      def calcula_saldo_entrada(self):
            saldo_conta_entrada = self.__saldo_inicial__ 
            saldo_conta_entrada += self.__entrada__
            print(f'O saldo total da sua conta é de: R$ {saldo_conta_entrada}')
            
      def calcula_saldo_saida(self):
            saldo_conta_saida = self.__saldo_inicial__
            saldo_conta_saida -= self.__saida__
            print(f'O saldo total da sua conta é de: R$ {saldo_conta_saida}')
            
extrato_conta = CalculaConta(58523684258, 500, 300, 100)

validar_usuario = extrato_conta.validar_usuario()
# Usuário verificado

saldo_entradas = extrato_conta.calcula_saldo_entrada()
# O saldo total da sua conta é de: R$ 800     

saldo_saidas = extrato_conta.calcula_saldo_saida()
# O saldo total da sua conta é de: R$ 400'''





            
'''______________HERANÇA - ERRADO_____________________'''

'''class Viagens:
      def __init__(self, cidade, estado, pais):
            self.cidade = cidade
            self.estado = estado
            self.pais = pais
            
      def get_cidade(self):
            return f'A cidade escolhida foi {self.cidade}'
      
      def get_estado(self):
            return f'A cidade escolhida foi {self.estado}'
      
      def get_pais(self):
            return f'A cidade escolhida foi {self.pais}'
      
class ValorPassagem(Viagens):
      def __init__(self, cidade, estado, pais, valor_passagem):
            self.valor_passagem = valor_passagem
            
            super().__init__(cidade, estado, pais)
      
      def passagem_barata_ou_cara():
            if self.valor_passagem > 300:
                  return f'A passagem para {self.cidade}está muito cara.'
            else:
                  return f'A passagem para {self.cidade}está barata.Podemos comprar'
            
            
verifica_valor_passagem = ValorPassagem('Florianópolis', 'Santa Catarina', 'Brasil', 600.00)
print(ValorPassagem.passagem_barata_ou_cara())'''



                  
                  

      
'''______________ENCAPSULAMENTO_____________________'''

'''class MostraEstado:
      def __init__(self, estado_da_agua):
            self.estado_da_agua = estado_da_agua
            
      def agua(self):
            print(f'O estado da água neste momento é {estado_da_agua}.')
            
class MudancaNoEstado(MostraEstado):
      def __init__(self,):
            super().__init__()
      
      def agua(self):
            print('A água está quente neste momento.')
            
agua_quente = MudancaNoEstado
agua_quente.agua(quente)'''
      


                        
                        

            
            
                  
            

            

