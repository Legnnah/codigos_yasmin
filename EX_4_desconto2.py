# Faça uma atualização no código do exercício anterior, agora o programa deve exibir o nome do produto, o valor do desconto e o valor final do produto.

# OUTPUT ESPERADO:

# Produto: FIAT TORO
# Preço: 200000
# Porcentagem de desconto: 15
# O FIAT TORO com 15.0% de desconto custará R$ 170000.0

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------


cliente = input("Digite o seu nome: ")
nome_produto = input("Digite o nome do veículo desejado: ")
produtopreco = float(input("Informe o preço do produto: "))
porcentagem = float(input("Qual a porcentagem de desconto?"))
desconto = produtopreco * (porcentagem / 100)
preco_final = produtopreco - desconto

print(f"Olá cliente {cliente}!")
print(f"O produto {nome_produto} custa R${produtopreco} e com o desconto de {desconto}%, custará R${preco_final} 🚗💸.")