# Escreva um programa que pede ao usuário o nome, idade, e-mail e senha para um cadastro e depois exiba as informações na tela:

# OUTPUT ESPERADO:

# | ------------------------------ |
# | ---------- CADASTRO ---------- |
# | ------------------------------ |
# | Nome: Maria
# | Idade: 17
# | Email: maria@email.com
# | Senha: 123123

# | ------------------------------ |
# | ----- USUÁRIO CADASTRADO ----- |
# | Seja bem vindo(a) Maria!
# | Email: maria@email.com
# | ------------------------------ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print("---------- CADASTRO ---------- ")
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
email = input("Informe o seu email: ")
senha = int(input("Digite a sua senha, por gentileza: "))

print("----- USUÁRIO CADASTRADO -----")
print(f"Seja bem vindo(a) {nome}")
print(f"Email: {email}")
