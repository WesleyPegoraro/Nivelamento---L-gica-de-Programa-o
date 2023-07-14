n = int(input("Digite um número: "))

i = 1

while True:
    mult = i * n
    print(f"{n} X {i} = {mult}")
    i = i + 1
    if i > 10:
        break