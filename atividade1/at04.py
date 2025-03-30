d = int(input("Quantos dias o carro foi alugado? "))
k = float(input("Quantos km foram percorridos? "))

if k > 100:
    c = d * 90 + (k - 100) * 12
else:
    c = d * 90

print(f"Valor total a pagar pelo aluguel: {c}")