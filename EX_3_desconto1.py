# Escreva um programa que pede ao usuário o preço de um produto e o valor de desconto em % e depois informe qual será o valor do desconto.
# Dica: 
# use a fórmula 
# desconto = preco * (porcentagem / 100) 
# para calcular o valor do desconto 

# OUTPUT ESPERADO:

# Qual o preço do produto? 300
# Qual a porcentagem de desconto? 10
# O produto que custa R$300.0 terá R$30.0 de desconto.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
cliente = input("Digite o seu nome: ")
produtopreco = float(input("Informe o preço do produto: "))
porcentagem = float(input("Qual a porcentagem de desconto?"))
desconto = produtopreco * (porcentagem / 100)
preco_final = produtopreco - desconto

print(f"Boa tarde {cliente}, seja bem vindo(a) ao nosso mercado 🛒.")
print(f"O produto que custa R${produtopreco}, terá o desconto de R${desconto}. Espero que você aproveite a sua compra com esse super desconto {cliente} ✨✨✨.")
print(f"O Total da compra foi de {preco_final}")