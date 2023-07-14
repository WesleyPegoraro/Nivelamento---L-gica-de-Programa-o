# Função que retorna uma msg de aprovado ou nao no exame
def msg_aprovado_exame(m):
    if m < 5:
        return "Reprovado em exame com média " + str(m)
    else:
        return "Aprovado em exame com média " + str(m)
    

# Status de aprovação ou não do aluno após o exame
#    if media_exame < 5:
#        print(f"Reprovado em exame com média {media_exame:.1f}")
#    else:
#        print(f"Aprovado em exame com média {media_exame:.1f}")