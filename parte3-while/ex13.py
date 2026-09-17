senha = "senai123"

while  True:
    entrada = input("Digite a senha: ")
    if entrada == senha:
        print("Acesso liberado!")
        break
    else:
        print("Senha incorreta. Tente novamente.")