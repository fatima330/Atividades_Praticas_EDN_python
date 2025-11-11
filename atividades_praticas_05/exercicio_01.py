def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    """
    Calcula o valor da gorjeta baseada no total da conta e na porcentagem desejada.

    Parâmetros:
        valor_conta (float): O valor total da conta.
        porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%).

    Retorna:
        float: O valor da gorjeta calculada.
    """
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta


# Exemplo de uso:
conta = 200.00
porcentagem = 10
valor_gorjeta = calcular_gorjeta(conta, porcentagem)

print(f"Valor da conta: R${conta:.2f}")
print(f"Gorjeta ({porcentagem}%): R${valor_gorjeta:.2f}")
print(f"Total a pagar: R${conta + valor_gorjeta:.2f}")

