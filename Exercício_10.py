# Ler um valor e escrever se é positivo ou negativo (considere o valor zero como positivo)

numero_str = input("Digite um número: ")

# 2. Tenta converter a entrada para um número inteiro e verifica se é positivo ou negativo
try:
    numero = int(numero_str) # Converte a string digitada para um número inteiro
    # Verifica se o número é maior ou igual a zero
    if numero >= 0:
        print(f"O número {numero} é POSITIVO.")
    else:
        print(f"O número {numero} é NEGATIVO.")

except ValueError:
    # Captura o erro se o usuário digitar algo que não é um número
    print("Entrada inválida. Por favor, digite um número inteiro.")


    


