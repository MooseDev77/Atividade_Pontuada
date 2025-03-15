import os
os. system ("clear")
#Uma financeira usa o seguinte critério para conceder empréstimos:
#o valor total do empréstimo deve ser até dez vezes o valor da renda mensal do solicitante
#e o valor da prestação deve ser no máximo 30% da renda mensal do solicitante.
#Escreva um programa que leia a renda mensal de um solicitante, o valor total do empréstimo
#solicitado e o número de prestações que o solicitante deseja pagar e informe se o empréstimo pode ou não ser concedido.


valor_emprestimo = float(input("Informe o valor do impréstimo: "))
renda_mensal = float(input("Informe a renda mensal: "))
valor_prestação = int(input("Informe o valor da prestações: "))

emprestimo = renda_mensal * 10
prestação = valor_emprestimo / valor_prestação
desconto_prestação = renda_mensal * 0.3

if valor_emprestimo <= emprestimo and valor_prestação <= prestação:
    print(f"Empréstimo Concedido. ")
else:
    print(f"Não Concedido. ")    
