import os
os. system ("clear")

#Faça um algoritmo para ler: a descrição do produto (nome),a quantidade adquirida e o preço unitário.
#Calcular e escrever o total (total = quantidade adquirida * preço unitário),
#o desconto e o total a pagar (total a pagar = total - desconto), sabendo-se que: 
# - Se quantidade <= 5 o desconto será de 2% 
# - Se quantidade > 5 e quantidade <= 10 o desconto será de 3% 
# - Se quantidade > 10 o desconto será de 5%.


print ("""
        Duna: 1° livro          Duna: 2° livro
            R$69,93                 R$57,52
            16 uni                  13 uni
""")

Duna = str(input("Qual livro deseja: ")).lower()
quantidade = input("Quantas unidades deseja: ")

match Duna:

    case 1:
        resultado1 =  quantidade * 69.93 
        resultado2 =  quantidade * 69.93
        resultado3 =  quantidade * 69.93
        if quantidade > 10:
            desconto = (quantidade * 69.93)*0.05
            print(f"{quantidade} livros Duna: 1° livro vai custar R${resultado1}. ")
              
        if quantidade > 5 or 10:
            desconto = (quantidade * 69.93)*0.03
            print(f"{quantidade} livros de Duna: 1° livro vai custar R${resultado2}. ")
           
        if quantidade <= 5:
            desconto = (quantidade * 69.93)*0.02
            print(f"{quantidade} livro de Duna: 1° livro vai custar R${resultado3}. ")
            

    case duna2:
        resultado4 = quantidade * 57.52 
        resultado5 = quantidade * 57.52
        resultado6 = quantidade * 57.52
        if quantidade > 10:
            desconto = (quantidade * 57.52)*0.05
            print(f"{quantidade} livros Duna: 1° livro vai custar R${resultado4}. ")
       
        if quantidade > 5 and 10:
            desconto = (quantidade * 57.52)*0.03
            print(f"{quantidade} livros de Duna: 1° livro vai custar R${resultado5}. ")
       
        if quantidade <= 5:
            desconto = (quantidade * 57.52)*0.02
            print(f"{quantidade} livro de Duna: 1° livro vai custar R${resultado6}. ")
       