'''
Lista de exercícios de fixação
Inicie o shell ou interpretador do Python, para fazer alguns dos exercícios desta lista.
1) O Python trabalha tipos de valores. Com os valores abaixo, dê o nome de seus tipos:
a. 1
b. 12.6
c. True
d. False
e. -543
f. -5.78
g. “copo”
h. ‘Belo dia’
2) Digite cada linha abaixo no shell do Python e informe quais estão corretos e quais
apresentam erro:
1
1a
a1
1.
.2
-.3
'agua"limpa'
"agua""
"""teste 1 2 3"""
3) Determine qual é o resultado dos seguintes cálculos no Python:
a. Operadores matemáticos
i. 10 + 3
ii. 10 - 3
iii. 10 * 3
iv. 10 / 3
v. 10 / 3.0
vi. 13 / 3
vii. 13 / 3.0
viii. 13 // 3.0
b. Ordem dos operadores
i. 5 + 30 * 20
ii. (5 + 30) * 20
iii. ((5 + 30) * 20) / 10
iv. 5 + 30 * 20 / 10
c. Operadores comparação
i. 2 < 3
ii. 9 > 8
iii. 1 == 1
iv. 1 != 2
v. 1 != 1
vi. 4 <= 4
vii. 5 >= 6
viii. 1 < 2 < 3
ix. 1 < 2 < 2
x. 1 + 2 < 25 / 5
d. Mais operadores matemáticos:
i. 2 ** 4
ii. 26 % 5
e. Operadores lógicos
i. not True
ii. not False
iii. True and True
iv. True and False
v. False and True
vi. False and False
vii. True or True
viii. True or False
ix. False or True
x. False or False
xi. True or True and False
xii. (True or True) and False
xiii. not True or False
xiv. not (True or False)
xv. not (True and False) and (True or False)
xvi. 1 > 2 and 3 > 4
xvii. 1 > 2 and 3 < 4
xviii. 1 < 2 and 3 < 4
xix. 1 + 2 and 3 + 4
xx. 1 + 2 or 3 + 4
xxi. True and 3 > 5
xxii. False and 3 >5
4) Qual será o valor final de x?
x = 10
x = x + 10
x = 100 - x
5) Resolva estes problemas em Python, guardando os valores e seus resultados em
variáveis diferentes.
a. Calcule a área de um quadrado cujo lado seja 2 cm.
b. Uma mala custa R$120,00. Esta recebeu 5% de desconto. Quanto você irá pagar
por ela.
c. Um carro está viajando a uma velocidade média de 100 Km/h o trecho de viagem
será 200 Km. Quantas horas irá demorar a viagem.
d. João tem 2 pirulitos, Maria 3 pirulitos e Sofia 1 pirulito. Calcule o total de pirulitos e
sua média.
e. Davi tem 13 anos e sua irmã tem 7 anos. Guarde na variável eh_mais_velho a
verificação se a idade de Davi é maior que a idade de sua irmã.
6) Qual será o valor de z? Qual seria outra forma de escrever este trecho de código?
z = 3
z += 2
z *= 6
z /= 5
7) Considere as seguintes variáveis:
ovo = 3.4
caju = 12.4
Qual será o valor de resposta em cada linha:
resposta = ovo if 1 > 2 else caju
resposta = ovo if ovo > caju else caju
resposta = ovo if ovo < caju else caju
resposta = 100 if ovo + caju > 15 else 200
resposta = 100 if ovo == 3 else 0
8) Qual é o resultado deste problema? Qual é o valor final da variável fim?
ab = 10
Ab = 20
aB = 30
AB = ab + Ab - aB
fim = AB + 1
9) Qual é o resultado de cada linha de comando do Python? Siga a ordem dos comandos.
valor = input("Informe um valor: ")
print("Valor informado: ", valor)
tipo = type(valor)
x_str = "123"
x = int(x)
xf = float(x)
sao_iguais = x == xf
print("Um float é igual a um int?", sao_iguais)
10) Crie o seguinte programa Python no arquivo lista03_02.py: Colete o nome da
pessoa, a cidade de nascimento dela, e o ano em que ela nasceu. Depois você irá mostrar
os dados coletados em linhas diferentes. E também, deverá informar quantos anos a
pessoa terá no ano 2030.
11) Programa Python no arquivo ex11.py: Este programa irá calcular a área de um
quadrado. Peça para a pessoa informar a medida numérica de um lado do quadrado. E
depois informe-lhe o valor da área do quadrado.
12) Programa Python no arquivo ex12.py: Este programa irá calcular a área de um
triângulo. Peça para a pessoa informar a medida numérica da base do triângulo, depois
colete o valor da altura. Apresente o valor da área do triângulo.
13). Crie o seguinte programa Python no arquivo ex13.py: Colete a idade de 3 pessoas e
mostre a média de suas idades.
14) Crie o seguinte programa Python no arquivo ex14.py: Colete a idade de duas pessoas.
E informe se a primeira idade é maior do que a da primeira. Neste aqui, basta responder
True para informar que a primeira idade é maior que a primeira.
15). Para o programa Python no arquivo ex15.py: Em uma casa, uma família decidiu dividir
o valor da conta de energia entre os moradores da casa. No programa eles informam o
valor da conta de energia e quantos que irão pagar a conta no mês. O programa calculará
quanto cada um deverá contribuir com a conta de energia.
16). Programa ex16.py: Estou tentando entender os juros do meu banco. Para isto, ele me
informou esta fórmula:
valor_final = valor_emprestimo + (valor_emprestimo * taxa * tempo)
onde que:
● valor_emprestimo: É o valor que pegarei emprestado.
● taxa: É o valor da taxa por mês. Por exemplo: se for 4% ao mês, o valor será 0.04.
● tempo: Quantidade de meses que irei pagar o empréstimo.
Crie um programa que colete cada um destes valores para calcular o valor final que estarei
pagando ao banco.
17) Desafio ex17.py: Dada uma equação de segundo grau, calcule suas raízes utilizando a
fórmula de Bhaskara.
18) Faça um programa que leia a nota de um aluno. Garanta que a nota seja um
valor inteiro entre zero e 100. Se o valor não estiver neste intervalo, informe que a
nota é inválida. Se a nota for maior que 60, informa que o aluno foi aprovado; caso
contrário, informa que ele foi reprovado.
19). Um vendedor ganha uma comissão de uma venda da seguinte forma: Se a
venda for …
● menor que R$1000,00, o vendedor não ganha nenhuma comissão;
● entre R$1.000,00 e R$5.000,00, o vendedor ganha uma comissão de 10% da
venda;
● entre R$5.000,00 e R$10.000,00, a comissão será de 20% da venda;
● entre R$10.000,00 e R$50.000,00 a comissão será de 25% da venda;
● acima de R$50.000,00 a comissão será de 30% da venda.
Faça um programa que informe o valor da comissão do vendedor para uma venda.
20) Crie um programa para calcular o valor a ser pago para um determinado produto para a
empresa NaoQueroMuitoSeuDinheiro. O pessoal desta empresa pediu o seguinte:
● Vamos coletar três valores:
○ O valor inicial da parcela.
○ O valor percentual de cada parcela.
○ A quantidade de parcelas.
● Para cada parcela a ser paga, o cálculo é o seguinte:
valor_parcela = valor_anterior + (valor_anterior *
percentual)
● No caso da primeira parcela, o valor anterior é o valor inicial.
Crie um programa que irá mostrar cada parcela e o seu valor. Por exemplo: se o valor inicial
for $100,00, o valor do percentual for 0,10, e a quantidade de parcelas for 2; logo nosso
programa irá mostrar:
Parcela 1: $ 110.0
Parcela 2: $ 121.0
21. O pessoal da empresa Caça-Clientes trabalha com ligações para números aleatórios.
Eles recebem uma lista com vários intervalos de números para eles ligarem. Na lista
recebida, você tem o prefixo do telefone, o primeiro sufixo e o último sufixo. Crie um script
que liste todos os números dos telefones, ao serem informados, o prefixo e os sufixos. Por
exemplo, suponha que o prefixo seja “3232” e que o primeiro prefixo seja “0001” e o último
sufixo seja “0005”; logo o programa irá imprimir:
Seus números de telefone são:
● 3232-0001
● 3232-0002
● 3232-0003
● 3232-0004
● 3232-0005
22). Crie um script que leia 10 números inteiros positivos e que irá apresentar:
● A lista dos valores lidos de forma ordenada.
● A contagem de cada item. Por exemplo, se o usuário informou [1,1,1,1,2, 3],
aqui apresentamos:
○ 1: 4x.
○ 2: 1x.
○ 3: 1x.
● Uma saída identificando o número, se o número é par e se é primo. Isto será feito
separando por vírgulas: Por exemplo, se informou [1,2,3,6]. Iremos apresentar aqui:
○ 1,ímpar,não é primo
○ 2,par,é primo
○ 3,ímpar,é primo
○ 6,par,não é primo
23) Neste script você irá ler o nome de 4 alunos e suas notas e determinar qual
aluno possui a maior nota.
'''


# 5

# a)
l = 2
area_quadrado = 2*2
print(area_quadrado)

# b)
mala = 120.00
mala_com_desconto = 120.00 - (mala * 0.05)
print(mala_com_desconto)

# c)
velocidade_media = 100
trecho = 200
tempo_viagem = trecho / velocidade_media
print(f'A viagem terá duração de: {tempo_viagem} horas')

# d)
joao = 2
maria = 3
sofia = 1
total_pirulitos = joao + maria + sofia
media_pirulitos = total_pirulitos / 3

print(total_pirulitos)
print(int(media_pirulitos))

# e)
davi = 13
irma_davi = 7
eh_mais_velho = davi > irma_davi
print(eh_mais_velho)


# 15

valor_energia = float(input('Informe o valor da conta de energia:'))

print(type(valor_energia))

qtd_moradores = input('Quantos moradores:')
qtd_moradores = int(qtd_moradores)

print(type(valor_energia))

valor_para_cada = valor_energia / qtd_moradores

print(float(valor_para_cada))


