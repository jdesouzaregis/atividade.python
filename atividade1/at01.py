n1 = float(input("Digite a 1ª nota: "))
n2 = float(input("Digite a 2ª nota: "))
n3 = float(input("Digite a 3ª nota: "))

m1 = (n1 + n2 + n3) / 3
m2 = (n1 * 2 + n2 * 2 + n3 * 3) / 7
m3 = (n1 * 1 + n2 * 2 + n3 * 2) / 5

print(f"Média aritmética simples: {m1}")
print(f"Média ponderada (pesos 2,2,3): {m2}")
print(f"Média ponderada (pesos 1,2,2): {m3}")
