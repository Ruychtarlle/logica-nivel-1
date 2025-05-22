#  Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior deles.

valor1 =int(input("Informe o primeiro numero\n"))
valor2 =int(input("Informe o segundo numero\n"))
valor3 =int(input("Informe o terceiro numero\n"))

#verificar o valor maior

maior = valor1
if valor2 > maior:
    maior = valor2
if valor3 > maior:
    maior = valor3
#Escrever o maior valor 
print("O maior valor é:",maior)
