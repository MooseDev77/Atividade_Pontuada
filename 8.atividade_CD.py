import os
os. system ("clear")


#Em uma loja de CD´s existem apenas quatro tipos de preços que estão associados a cores
#Assim os CD´s que ficam na loja não são marcados por preços e sim por cores.
#Desenvolva o algoritmo que a partir da entrada da cor o software mostre o preço.
#A loja está atualmente com a seguinte tabela de preços. 
print ("""
       Cor         Preço       
      Azul        R$ 20,00
      Vermelho    R$ 40,00
      Verde       R$ 10,00 
      Amarelo     R$ 30,00  """)
        
CD = str (input("Qual CD você escolhe de acordo com a cor: "))

match CD:
    case "Azul":
        print ("O valor desse disco é: R$ 20,00")
    case "Vermelho":
        print ("O valor desse disco é: R$ 40,00")  
    case "verde":
        print ("O valor desse disco é: R$ 10,00")
    case "Amarelo":
        print ("O valor desse disco é: R$ 30,00")

