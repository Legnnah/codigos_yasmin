# Escreva um programa que pede ao usuário o valor atual da cotação do dollar e a quantidade de dólares para ser convertido em reais. 
# Depois mostre na tela a conversão.

# OUTPUT ESPERADO:

# Digite a cotação do dollar: 5.60
# Digite o valor em dollar a ser convetido para real: 100
# O valor em reais é:  560.0

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

usuario = input("Digite o seu nome de usuário, por gentileza: ")
print(f"Olá usuário {usuario}. Este é um programa que converte dollar em real.")

cotacao = float(input("Digite a cotação em dollar: "))
valor = float(input("Digite o valor em dollar a ser convetido para real: "))

print(f"Ao ser convertido, o valor em reais é de R${valor} 🪙.")
