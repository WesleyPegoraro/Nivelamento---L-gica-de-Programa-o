# Criação da função com parâmetro
def maior2n(num1, num2):
    if num1 > num2:
        maior = num1
    else:
        maior = num2
    return maior

# Programa principal
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
print("Maior numero: ", maior2n(n1,n2))