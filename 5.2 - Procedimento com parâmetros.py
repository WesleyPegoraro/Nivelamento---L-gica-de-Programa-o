# Subalgoritmos - Criação do procedimento
def saudacao(hora):
    if hora < 12:
        msg = "Bom dia,"
    elif hora < 18:
        msg = "Boa tarde,"
    else:
        msg = "Boa noite,"
    print(msg,"seja bem vindo à FIAP!")

# Programa principal - Chamada do procedimento
saudacao(20)