nomeProduto = str(input('Digite o nome do produto: '))
preco = float(input('Digite o preco do produto R$: '))
quantidade = int(input('Digite a quantidade do produto: '))

total =  preco * quantidade  

print('produto:', nomeProduto ) 
print(f'Valor unitario: {preco:.2f}')
print( 'Quantidade:', quantidade)
print(f'Preço Total R$: {total:.2f}')

