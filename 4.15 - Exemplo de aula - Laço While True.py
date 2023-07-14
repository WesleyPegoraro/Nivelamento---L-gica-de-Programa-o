# SAÍDA:
#   Intervalo: 3 4 5 6 7 8 9 

ini = int(input("Digite o número inicial: "))
f = int(input("Digite o valor final"))

while True:
    print(ini, " ")
    ini = ini + 1 #ini += 1
    if ini > f:
        break