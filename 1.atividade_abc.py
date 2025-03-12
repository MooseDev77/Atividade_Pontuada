import os
os. system ("clear")

#Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C,
#caso contrário, imprima que a A + B é maior que C. 

valor_1 = int(input("Digite o primeiro numero: "))
valor_2 = int(input("Digite o segundo numero: "))
valor_3 = int(input("Digite o terceiro numero: "))

soma = valor_1 + valor_2
print(f"\nresultado: {soma}")

if soma < valor_3:
    
    print (f"A e B é menor que C")
else:
    print (f"A e B é maior que C")

