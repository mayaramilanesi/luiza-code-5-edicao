
def aprovado_reprovado(nota_aluno):
      if nota_aluno >= 100:
            return 'O intervalo precisa ser entre zero e 100'
      elif nota_aluno >= 60:
            return 'O aluno foi aprovado'
      else:
            return 'O aluno foi reprovado'
      
print(aprovado_reprovado(110))