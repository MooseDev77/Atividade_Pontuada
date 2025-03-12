import os
os. system ("clear")

#Faça um algoritmo que leia dois valores inteiros A e B se os valores forem iguais
#deverá se somar os dois, caso contrário multiplique A por B. Ao final de qualquer um dos cálculos
#deve-se atribuir o resultado para uma variável C e mostrar seu conteúdo na tela.
        

numero_1 = int(input("Digite o primeiro numero: "))
numero_2 = int(input("Digite o segundo numero: "))

if numero_1 and numero_2 == numero_1 and numero_2:
    soma = numero_1 + numero_2
    print (f"resultado {soma}")
    
else:
    soma = numero_1 * numero_2    
    print (f"resultado: {soma}")
    