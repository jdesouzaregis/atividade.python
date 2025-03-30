v = float(input("Digite o valor total das mercadorias: "))

if v > 500:
    imp = (v - 500) * 0.5
else:
    imp = 0

print(f"Imposto devido: {imp}")