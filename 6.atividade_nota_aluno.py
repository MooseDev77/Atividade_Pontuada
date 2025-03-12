import os
os. system ("clear")

#Escreva um programa que leia do teclado as duas notas de um aluno, calcule e exiba a média 
#notas. O programa deve, adicionalmente, exibir uma mensagem de parabéns caso o aluno
#esteja aprovado (média superior ou igual a 6,0), média até 4,0, o aluno está em recuperação,
#caso a média seja inferior a 4,0 o aluno será reprovado.

nome = str(input("Informe o seu nome: "))
nota_1 = float(input("Informe a sua primeira nota: "))
nota_2 = float(input("Informe a sua segunda nota: "))
situação = str("Parabéns, Recuperação e Reprovado")

media = (nota_1 + nota_2) / 2
print(f"media: {media}")

if media >= 6:
     print("Parabéns")
elif media >= 4:
     print("Recuperação")
elif media  < 4:      
     print("Reprovado")




 
