nota_clara = float(input("Qual é a nota bimestral da aluna Clara?"))
nota_roberto = float(input("Qual é a nota bimestral do aluno Roberto?"))
nota_joice = float(input("Qual é a nota bimestral da aluna Joice?"))
nota_fernando = float(input("Qual é a nota bimestral do aluno Fernando?"))

soma = nota_clara + nota_roberto + nota_joice + nota_fernando
media = soma/4

if media >=7.0:
    print("Aprovado(a) ✅")
elif media >=5.0 and media < 7.0:
    print("Recuperação ⚠️")
else:
    print("Reprovado(a) ❌")

print(f"A média escolar é {media}!")