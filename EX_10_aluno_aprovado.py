# Escreva um código que pede a nota de duas provas do aluno e verifique se o aluno foi aprovado com as condições abaixo:
# O aluno precisa ter média maior que 7 e não pode ter tirado zero em nenhuma nota.
# Não é necessário usar estruturas condicionais, apenas expressões lógicas conforme estudado no material de expressões lógicas.

# OUTPUT ESPERADO:
# Exemplo 1:

# Digite a primeira nota: 10
# Digite a segunda nota: 8
# Aluno aprovado? True

# Exemplo 2:

# Digite a primeira nota: 10
# Digite a segunda nota: 0
# Aluno aprovado? False

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

nota_1 = float(input("Digite a sua primeira nota: "))
nota_2 = float(input("Digite a sua segunda nota: "))

soma = nota_1 + nota_2
media = soma / 2

print("-----------PRIMEIRA PROVA------------------")
print(f"A nota da primeira prova foi: {nota_1}")

print("-----------SEGUNDA PROVA------------------")
print(f"A nota da segunda prova foi: {nota_2}")
