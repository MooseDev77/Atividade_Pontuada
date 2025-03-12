import os
os. system ("clear")

#Faça um programa que leia um código de operação (+,-,* ou /), e também dois valores inteiros A e B. 
#O programa deve calcular o resultado da operação escolhida aplicado a A e B. Por exemplo, se a 
#operação escolhida foi * e A = 1 e B = 3, o programa deve fornecer como resultado o valor de 1*3, que é 3.

valor_1 = int(input("Informe o primeiro numero: "))
valor_2 = int(input("Informe o segundo numero: "))
operações = str(input("Escolha a operação: + - * /: "))

match operações: 
        case "+":
            Soma = valor_1 + valor_2
            print (f"\n1°: {valor_1}")
            print (f"2°: {valor_2}")
            print (f"R: {Soma}")
        case "-":
            Soma = valor_1 - valor_2
            print (f"\n1°: {valor_1}")
            print (f"2°: {valor_2}")
            print (f"R: {Soma}")
        case "*":
            Soma = valor_1 * valor_2
            print (f"\n1°: {valor_1}")
            print (f"2°: {valor_2}")
            print (f"{Soma}")
        case "/":
            Soma = valor_1 / valor_2
            print (f"\n1°: {valor_1}")
            print (f"2°: {valor_2}")
            print (f"R: {Soma}")


 
