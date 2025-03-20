#As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra

print("Se cada macãs custam R$ 1,30")
print("Se forem compradas menos de uma dúzia,é R$ 1,00")
quantidade = int(input("")) #digite a quantidade de maças para ver se aplica desconto ou não

if quantidade < 12: 
    preco = 1.30
else:
    preco= 1
    
    
total = quantidade * preco
print(f"Custo total da comprar é: =R${total:.2f}")
