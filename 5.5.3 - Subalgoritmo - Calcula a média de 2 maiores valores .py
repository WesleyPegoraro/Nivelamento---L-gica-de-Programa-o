def menor3n(n1, n2, n3):
    menor = n1
    if n2 < menor:
        menor = n2
    if n3 < menor:
        menor = n3
    return menor

# Função que calcula a media das 2 maiores notas
def media2maiores(n1, n2, n3):
    menor = menor3n(n1, n2, n3)
    return (n1 + n2 + n3 - menor) / 2



# Cálculo da media semestral com as duas notas maiores
# media_semestral = (nota1 + nota2 + nota3 - menor_nota) / 2
#   print(f"A sua Média Semestral é {media_semestral:.1f}")