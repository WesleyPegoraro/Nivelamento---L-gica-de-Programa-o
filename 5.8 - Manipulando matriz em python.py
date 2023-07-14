# MANIPULANDO MATRIZ - PYTHON

matriz = [[0,0],[0,0],[0,0],[0,0]]

# 1 - PREENCHER A MATRIZ
print("Preenchendo a matriz...")
for l in range(4):
    for c in range(2):
        matriz[l][c] = int(input(f"Matriz[{l}][{c}]= "))


# 2 - EXIBIR A MATRIZ
print("\nExibindo a matriz...")
for l in range(4):
    for c in range(2):
        print(f"{matriz[l][c]}\t", end = "")
    print()


# 3 - SOMAR OS ELEMENTOS DA MATRIZ
soma = 0
for l in range(4):
    for c in range(2):
        soma += matriz[l][c]

print("\nSoma = ", soma)