pares = 0
impares = 0

while True:
    entrada = input("Digite apenas numeros inteiros (ou 'fim' para encerrar):")

    if entrada == 'fim':
        break
    try:
        numero = int(entrada)

        if numero % 2 == 0:
            print(f"{numero} é par.")
            pares +=1
        else:
            print(f"{numero} é ímpar.")
            impares += 1


    except ValueError:
        print('Erro voce não digitou um numero inteiro! Tente de novo.')

print('programa encerrado!!')
print(f'Quantidade de numeros pares: {pares}')
print(f'Quantidade de numeros impares: {impares}')