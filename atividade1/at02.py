s = int(input("Digite um valor em segundos: "))

d = s // 86400
s %= 86400
h = s // 3600
s %= 3600
m = s // 60

print(f"O valor equivale a {d} dia(s), {h} hora(s) e {m} minuto(s)")