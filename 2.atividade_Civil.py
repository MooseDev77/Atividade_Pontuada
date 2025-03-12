import os
os. system ("clear")

#Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. 
#Caso sexo seja “F” e estado civil seja “CASADA”, solicitar o tempo de casada (anos).
#Por fim, mostre os dados do usuário.

nome = str(input("Informe o seu nome por favor: "))
sexo = str(input("Informe o seu sexo por favor: "))
match sexo:
    case "F":
        estado_civil = str(input("Casada ou solteira: ")) .upper()
match estado_civil:
            case "CASADA":
                tempo_casamento = int(input("Informe o tempo do casamento: "))
                print (f"\nom: {nome}")
                print (f"sexo: {sexo}")
                print (f"estado civil: {estado_civil}")
                print (f"tempo de casamento: {tempo_casamento}")
            case "Solteira":
                print (f"\nom: {nome}")
                print (f"sexo: {sexo}")
                print (f"estado civil: {estado_civil}")


        

