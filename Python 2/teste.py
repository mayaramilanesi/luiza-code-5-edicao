
class Humanos:
      sexo = 'feminino'
      
      def __init__(self, nome, idade, peso):
            self.nome = nome
            self.idade = idade
            self.peso = peso
      
      def description(self):
            print(f'{self.nome} tem {self.idade} anos e pesa {self.peso} Kg.')
            
      def action(self, metros):
            print(f'{self.nome} caminha {metros} metros por dia')
            
descricao = Humanos('Mayara', 28, 70.0).description
acao = Humanos('Ivani', 48, 73.5).action(5000)

print(descricao)
print(acao)
