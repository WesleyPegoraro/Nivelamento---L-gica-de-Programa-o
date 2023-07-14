# Função que retorna o menor entre 3 valores
def menor3n(n1, n2, n3):
    menor = n1
    if n2 < menor:
        menor = n2
    if n3 < menor:
        menor = n3
    return menor



# Verificação da menor entre 3 notas
# menor_nota = nota1
# if nota2 < menor_nota:
#   menor_nota = nota2
# if nota3 < menor_nota:
#   menor_nota = nota3