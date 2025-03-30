n = int(input("Digite um número inteiro maior que 1: "))
primo = True

if n > 1:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            primo = False
            break

if primo:
    print(f"O número {n} é primo.")
else:
    print(f"O número {n} não é primo.")