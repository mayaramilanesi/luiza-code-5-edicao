def emprestimo(valor_emprestimo, taxa, tempo):
      valor_final = valor_emprestimo + (valor_emprestimo * taxa * tempo)
      
      return valor_final

print(emprestimo(50000, 0.05, 5))

