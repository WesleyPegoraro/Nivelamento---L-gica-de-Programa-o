# SAÍDA 1:
# Você digitou S ou N
#
#
# Solicitar ao usuário que digite S para sim ou N para não obrigatoriamente.
# ENTRADA 2:
#   Digite [S]im ou [N]ão: H
# SAÍDA 2:
#   Você digitou 'H', digite S ou N!

opcao = input("Digite [S]im ou [N]ão: ")
while opcao != 's' and opcao != 'S' and opcao != 'n' and opcao != 'N':
    print("Você digitou:", opcao, "Digite S ou N!")
    opcao = input("Digite [S]im ou [N]ão: ")

print("Você digitou ", opcao)