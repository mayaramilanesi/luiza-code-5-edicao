from class_main import Friends

class Job(Friends):
      def __init__(self, person1, person2, person3, person4, person5, person6):
            super().__init__(person1, person2, person3, person4, person5, person6)
            
            
      def profissao(self):
            if self.person1 == 'Monica':
                  return f'{self.person1} é chefe de cozinha.'
            if self.person1 == 'Ross':
                  return f'{self.person1} é Paleontólogo.'
            if self.person1 == 'Rachel':
                  return f'{self.person1} é executiva de moda.'
            if self.person1 == 'Chandler':
                  return f'{self.person1} é publicitário.'
            if self.person1 == 'Joey':
                  return f'{self.person1} é ator'
            if self.person1 == 'Phoebe':
                  return f'{self.person1} é terapeuta massagista.'
            
profissao = Job('Monica', 'Chandler', 'Rachel', 'Ross', 'Phoebe', 'Joey')

print(profissao.profissao())
