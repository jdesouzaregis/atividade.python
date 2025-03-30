print("Os 100 primeiros números primos são:")
p = []
n = 2

while len(p) < 100:
    primo = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            primo = False
            break
    if primo:
        p.append(n)
    n += 1

print(", ".join(map(str, p)))