from class_main import Friends

class Bordoes(Friends):
      def __init__(self, person1, person2, person3, person4, person5, person6):
            super().__init__(person1, person2, person3, person4, person5, person6)
            
      def phrases(self):
            if self.person1 == 'Monica':
                  return 'I KNOW!.'
            if self.person1 == 'Ross':
                  return 'Unagi.'
            if self.person1 == 'Rachel':
                  return 'NOOOOOO!'
            if self.person1 == 'Chandler':
                  return "I'm Chandler, I make jokes when I'm uncomfortable."
            if self.person1 == 'Joey':
                  return "How You Doin' ?"
            if self.person1 == 'Phoebe':
                  return "Hi, I’m Regina Phalange" 
            
bordoes = Bordoes('Monica', 'Chandler', 'Rachel', 'Ross', 'Phoebe', 'Joey')

print(bordoes.phrases())
