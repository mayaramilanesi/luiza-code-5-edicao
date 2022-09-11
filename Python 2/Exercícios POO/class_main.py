class Friends:
      def __init__(self, person1, person2, person3, person4, person5, person6):
            self.person1 = person1
            self.person2 = person2
            self.person3 = person3
            self.person4 = person4
            self.person5 = person5
            self.person6 = person6
            
      def get_persons(self):
            return f'Friends é uma série de comédia com os personagens: {self.person1}, {self.person2}, {self.person3}, {self.person4}, {self.person5} e  {self.person6}.'
      
      def skill(self, name, skill):
            self.name = name
            self.skil = skill
            return f'{self.name} gosta de {self.skil}.'
      
      def friend_friends(self, sim_ou_nao):
            self.resposta = sim_ou_nao
            if self.resposta == 'sim':
                  return 'Você pode entrar na casa da Mônica.'
            return 'Você não pode entrar na casa da Mônica.'
      
      def phrases(self):
            return "I'll be there for you ????"
      
friends = Friends('Monica', 'Chandler', 'Rachel', 'Ross', 'Phoebe', 'Joey').get_persons()
print(friends)
      