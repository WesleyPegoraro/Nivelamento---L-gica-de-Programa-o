# Função booleana que verifica se uma nota é válida ou não
def nota_valida(nota):
    if nota >= 0 and nota <= 10:
        return True
    else:
        return False
    

    
# if nota1 >=0 and nota1  <= 10:
# else:
#   print (f"Nota 1: {nota1} - É inválida!")