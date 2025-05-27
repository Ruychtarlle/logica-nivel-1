# Ler um valor e escrever a mensagem É MAIOR QUE 10! se o valor lido for maior que 10, caso contrário escrever NÃO É MAIOR QUE 10!

valor_str = input("Digite um número: ")

# 2. Converter o valor digitado (que é uma string) para um número inteiro
# É importante usar um bloco try-except para lidar com entradas não numéricas
try:
    valor = int(valor_str)

    # 3. Verificar se o valor é maior que 10
    if valor > 10:
        print("É MAIOR QUE 10!")
    else:
        print("NÃO É MAIOR QUE 10!")

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")
