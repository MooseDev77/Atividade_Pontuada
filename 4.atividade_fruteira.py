import os
os. system ("clear")

#Uma fruteira está vendendo frutas com a seguinte tabela de preços: 
#Se o cliente comprar a partir de 10 Kg em frutas ou o valor total da compra ultrapassar
#R$ 15,00, receberá ainda um desconto de 10% sobre este total.
#Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
#(em Kg) de maçãs adquiridas e escreva o valor a ser pago pelo cliente.

print ("""

                Morango                 |               maçã
      R$ 1,50 por kg (até 5kg)          |       R$ 2,80 por kg (até 5kg)
      R$ 1,20 por kg (acima de 5kg)     |       R$ 2,50 por kg (acima de 5kg) 

""")

Fruta = input("Qual fruta você deseja: ").lower()

match Fruta:
    case "maçã":
        quantidade = int(input("Informe a quantidade (em kg)"))
        resultado1 = quantidade * 2.80
        resultado2 = quantidade * 2.50
        if quantidade >= 10 or resultado2 > 15:
            desconto2 = (quantidade * 2.50)*0.1
            print (f"A quantidade de {quantidade}kg de maçã vai custar R${resultado2}. ")
        elif quantidade <= 5:
            print(f" A quantidade de {quantidade}kg de maçã vai custar R${resultado1}")
        elif quantidade < 5:
            resultado1 = quantidade * 2.50
            print(f"A quantidade de {quantidade} kg de maçã vai custar R${resultado1} ")

    case "morango":
        quantidade = int(input("Informe a quantidade (em kg)"))
        resultado3 = quantidade * 1.50
        resultado4 = quantidade * 1.20
        if quantidade >= 10 or resultado3 > 15:
            desconto2 = (quantidade * 1,20)*0.1
            print (f"A quantidade de {quantidade}kg de morango vai custar R${resultado3}. ")
        elif quantidade <= 5:
            print(f" A quantidade de {quantidade}kg de morango vai custar R${resultado4}")
        elif quantidade < 5:
            resultado4 = quantidade * 1.20
            print(f"A quantidade de {quantidade} kg de morango vai custar R${resultado4} ")    