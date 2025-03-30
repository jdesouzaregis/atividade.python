u = input("Digite o nome de usuário: ")
s = input("Digite a senha: ")

while u == s:
    print("Usuário e senha não podem ser iguais. Tente novamente.")
    u = input("Digite o nome de usuário: ")
    s = input("Digite a senha: ")

print("Cadastro realizado com sucesso!")