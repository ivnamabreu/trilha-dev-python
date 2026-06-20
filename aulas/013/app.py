tem_alta_renda = True
tem_bom_crédito = False
tem_grande_patrimonio = True
tem_historico_criminal = True

if tem_alta_renda and tem_bom_crédito:
    print('Elegível para empréstimo tipo A.')
if tem_alta_renda and (tem_bom_crédito or tem_grande_patrimonio):
    print('Elegível para empréstimo tipo B')
if (tem_alta_renda or tem_bom_crédito or tem_grande_patrimonio) and not tem_historico_criminal:
    print('Elegível para empréstimo tipo C.')