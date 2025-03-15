import os
os. system ("clear")

#Um posto está vendendo combustíveis com a seguinte tabela de descontos: 
#Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível
#(codificado da seguinte forma: A-álcool, G-gasolina),calcule e imprima 
#o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina
#é R$ 6,59 e o preço do litro do álcool é R$ 3,79. 

Litros = float (input("Qual a quantidade de litros que deseja: "))
tipo_combustivel = input ("Escolha o tipo de combustivel (G- Gasolina: | A- Alcool)") .strip() .upper()

Gasolina = 6.59
Alcool = 3.79

match tipo_combustivel:
    case "A":
        preço_por_litro = Alcool
        desconto = 0.2 if Litros <= 25 else 0.4
    case "G":
        preço_por_litro = Gasolina
        desconto = 0.3 if Litros <= 25 else 0.5
    case _:
        print ("Opção Inválida! ")

valor_total = preço_por_litro * Litros
valor_desconto = valor_total * desconto
valor_pago = valor_total - valor_desconto

print (f"Valor a ser pago é: {valor_pago}")

