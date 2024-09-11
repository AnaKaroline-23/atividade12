# Crie um programa que receba a nota de um aluno e informe se ele foi aprovado ou reprovado. Considere que a média para aprovação é 7.
nota = int(input(f" nota do aluno "))
if nota >=7:
    print(f"Aprovado")

elif nota <7:
    print(f"Reprovado")
