s = float(input("Digite o salário inicial: "))
a = float(input("Digite o aumento percentual anual: "))
anos = int(input("Digite a quantidade de anos: "))

for i in range(anos):
    s += s * (a / 100)
    a *= 2

print(f"Salário atual após {anos} anos: {s}")