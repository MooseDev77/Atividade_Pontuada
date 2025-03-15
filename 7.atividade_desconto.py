import os
os. system ("clear")

#Faça um algoritmo para ler: a descrição do produto (nome),a quantidade adquirida e o preço unitário.
#Calcular e escrever o total (total = quantidade adquirida * preço unitário),
#o desconto e o total a pagar (total a pagar = total - desconto), sabendo-se que: 
# - Se quantidade <= 5 o desconto será de 2% 
# - Se quantidade > 5 e quantidade <= 10 o desconto será de 3% 
# - Se quantidade > 10 o desconto será de 5%.


print ("""
     1\t Duna: 1° livro     2\t Duna: 2° livro
           R$69,93                R$57,52
            16 uni                 13 uni
  
""")
   
Duna = int(input("Qual livro deseja (1 ou 2): "))
quantidade = int(input("Quantas unidades deseja: "))

match Duna:

    case 1:
        total = quantidade * 69.93
        resultado1 =  quantidade * 69.93 
        resultado2 =  quantidade * 69.93
        resultado3 =  quantidade * 69.93
        if quantidade > 10:
            desconto = (quantidade * 69.93)*0.05
            print(f"\nFinalizando compra: \nproduto:{1} \nquantidade:{quantidade} \npreço:R${69.93} \ntotal:R${total:.2f} \ndesconto:R${desconto:.2f} \ntotal a pagar:R${total - desconto:.2f}")
           
        if quantidade > 5 or 10:
            desconto = (quantidade * 69.93)*0.03
            print(f"\nFinalizando compra: \nproduto:{1} \nquantidade:{quantidade} \npreço:R${69.93} \ntotal:R${total:.2f} \ndesconto:R${desconto:.2f} \ntotal a pagar:R${total - desconto:.2f}")
           
        if quantidade <= 5:
            desconto = (quantidade * 69.93)*0.02
            print(f"\nFinalizando compra: \nproduto:{1} \nquantidade:{quantidade} \npreço:R${69.93} \ntotal:R${total:.2f} \ndesconto:R${desconto:.2f} \ntotal a pagar:R${total - desconto:.2f}")
            

    case 2:
        total2 = quantidade * 57.52
        resultado4 = quantidade * 57.52 
        resultado5 = quantidade * 57.52
        resultado6 = quantidade * 57.52
        if quantidade > 10:
            desconto = (quantidade * 57.52)*0.05
            print(f"\nFinalizando compra: \nproduto:{2} \nquantidade:{quantidade} \npreço:R${57.52} \ntotal:R${total2:.2f} \ndesconto:R${desconto:.2f} \ntotal a pagar:R${total2 - desconto:.2f}")
       
        if quantidade > 5 and 10:
            desconto = (quantidade * 57.52)*0.03
            print(f"\nFinalizando compra: \nproduto:{2} \nquantidade:{quantidade} \npreço:R${57.52} \ntotal:R${total2:.2f} \ndesconto:R${desconto:.2f} \ntotal a pagar:R${total2 - desconto:.2f}")
       
        if quantidade <= 5:
            desconto = (quantidade * 57.52)*0.02
            print(f"\nFinalizando compra: \nproduto:{2} \nquantidade:{quantidade} \npreço:R${57.52} \ntotal:R${total2:.2f} \ndesconto:R${desconto:.2f} \ntotal a pagar:R${total2 - desconto:.2f}")
 