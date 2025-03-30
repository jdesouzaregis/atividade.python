t = int(input("Quantas turmas existem? "))
a = int(input("Qual o total de alunos? "))

m = a / t

if m > 40:
    print(f"Alguma turma tem mais de 40 alunos. Média de alunos por turma: {m}")
else:
    print(f"Média de alunos por turma: {m}")