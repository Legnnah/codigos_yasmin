# Escreva um programa que pede ao usuário o nome de um aluno e as notas de 3 provas que este aluno realizou.
# No fim o programa deve mostrar na tela a média das 3 provas
# Dica:
# Para calcular a média das provas você deve dividir a soma das notas das provas pela quantidade de provas realizadas
# media = soma / 3

# OUTPUT ESPERADO:

# | ______________________________ |
# | SISTEMA DE PROVAS
# | ______________________________ |
# | Nome do aluno: Fulano
# | Nota da primeira prova: 9.8
# | Nota da segunda prova: 7
# | Nota da terceira prova: 8.5
# | ______________________________ |
# | Aluno: Fulano 
# | Média: 8.43
# | Aluno aprovado
# | ______________________________ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
print("SISTEMA DE PROVAS 📄")
aluno = input("Digite o nome do aluno, por favor: ")
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))

print(f"Nome do aluno: {aluno}")
print(f"Nota da primeira prova: {nota_1}")
print(f"Nota da segunda prova: {nota_2}")
print(f"Nota da terceira prova: {nota_3}")

print(f"Aluno: {aluno}")
print(f"Média: {media}")
print("Aluno aprovado")

soma = nota_1 + nota_2 + nota_3
media = soma / 3

