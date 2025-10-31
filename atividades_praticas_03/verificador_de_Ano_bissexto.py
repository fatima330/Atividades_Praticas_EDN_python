ano_bissexto = int(input("Digite um ano: "))
if (ano_bissexto % 4 == 0 and ano_bissexto % 100 != 0) or (ano_bissexto % 400 == 0):
    print(f"O ano {ano_bissexto} é bissexto.")