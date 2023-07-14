# Dados 2 números, exibir os números do intervalo
# ENTRADA:
#   Digite 2 números: 3 9
# SAÍDA:
#   Intervalo: 3 4 5 6 7 8 9

ini = int(input("Digite o número inicial: "))
f = (int(input("Digite o número final: ")))

for cont in range(ini, f + 1, 1):
    print(cont, "")
