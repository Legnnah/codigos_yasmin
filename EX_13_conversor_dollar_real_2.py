# Atualize o código do exercício de conversor de dollar para real. Agora um "MENU" de opções aparecerá na tela pedindo ao usuário que escolha se quer converter
# de Reais para Dollar ou Dollar para reais. O usuário deve digitar a opção antes de informar os valores.

# OUTPUT ESPERADO:

#------- Exemplo 1 (Dólares para Reais):

# Escolha uma opção: 
# 1 - Dollar para Real
# 2 - Real para dollar
# Digite a opção: 1
# Informe a cotação atual do Dollar: 5.65
# Informe a quantidade de dólares: 150 
# O valor em reais é R$847.50

#---------- Exemplo 2 (Reais para Dólares)

# Escolha uma opção: 
# 1 - Dollar para Real
# 2 - Real para dollar
# Digite a opção: 2
# Informe a cotação atual do Dollar: 5.65
# Informe a quantidade de reais: 150
# O valor em dólares é $26.55

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
usuario = input("Digite o seu nome de usuário, por gentileza: ")
print(f"Olá usuário {usuario}. Este é um programa que converte dollar em real e vice-versa")

# Real
cotacao = float(input("Digite a cotação em dollar: "))
valor = float(input("Digite o valor em dollar a ser convetido para real: "))

print(f"Ao ser convertido, o valor em reais é de R${valor} 🪙.")

# Dollar 
cotacao = float(input("Digite a cotação em real: "))
valor = float(input("Digite o valor em real a ser convetido para dollar: "))

print(f"Ao ser convertido, o valor em dollar é de {valor} 🪙.")

