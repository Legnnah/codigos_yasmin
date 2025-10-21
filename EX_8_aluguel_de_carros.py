# Aluguel de carros:
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado

# OUTPUT ESPERADO:

# Por quantos dias o carro foi alugado: 10
# Quantos km o carro rodou: 500
# Você andou 500.0km por 10 dias, então o preço a pagar é R$675.00.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

dias_percorridos = int(input("Por quantos dias o carro foi alugado?"))
km_percorrido = float(input("Quantos km o seu carro percorreu?"))
diaria = 60
km = 0.15

# Diária
formula1 = diaria * dias_percorridos

# Km
formula2 = km * km_percorrido

# Valor 
formula3 = formula1 + formula2

print(f"Você andou {km_percorrido} por {dias_percorridos} dias, portanto o preço a pagar é: R${formula3}")