n = int(input("Digite um número ímpar: "))

if n % 2 == 0:
    print("Número inválido, por favor insira um número ímpar.")
else:
    a = (n - 2) ** 2
    p = (n + 2) ** 2
    d = p - a
    print(f"Diferença entre os quadrados: {d}")