nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

valor_final = preco_original * (1 - porcentagem_desconto / 100)
print(f"O preco final da {nome_produto} apos {porcentagem_desconto}% de desconto e: R$ {valor_final:.2f}")