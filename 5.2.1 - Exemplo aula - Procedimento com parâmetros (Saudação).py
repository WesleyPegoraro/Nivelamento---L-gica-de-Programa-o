# Subalgoritmos - Criação do procedimento com parâmetros
def saudacao2(usuario, hora):
    if hora < 12:
        msg = "bom dia! "
    elif hora < 18:
        msg = "boa tarde!"
    else:
        msg = "boa noite!"
    print("Olá " + usuario + ", " + msg + " Você está logado(a).")

# Programa principal - Chamada do procedimento
saudacao2("Flávia", 19)