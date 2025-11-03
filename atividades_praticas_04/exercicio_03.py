while True:
    senha = input(("Digite sua senha (ou 'sair' para encerrar):"))
    if senha ==  'sair':
        print('programa encerrado pelo usuario')
        break
    if len (senha) <= 8:
        print('senha fraca deve ter pelo menos 8 caracteres')
        continue

    tem_numero = False
    for caractere in senha:
        if caractere.isdigit():   
            tem_numero = True
            break             

    if not tem_numero:
        print("Senha fraca! Deve conter pelo menos um número.")
        continue

    print("Senha válida e forte!")
    break


