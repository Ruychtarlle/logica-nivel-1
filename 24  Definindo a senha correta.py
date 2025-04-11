# Definindo a senha correta

senha_correta = "123456"  # Você pode alterar para qualquer senha desejada

while True:
    # Solicitando a senha ao usuário
    senha = input("Digite a senha: ")
    
    # Verificando se a senha está correta
    if senha == senha_correta:
        print("Senha correta! Acesso liberado.")
        break  # Sai do loop quando a senha está correta
    else:
        print("Senha incorreta. Tente novamente.")
