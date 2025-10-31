nome = str(input("Digite o nome do vendedor: "))
salario_fixo = float(input("Digite o salário fixo de {}: ".format(nome)))
total_vendas = float(input("Digite o valor total das vendas realizadas por {}: ".format(nome)))

comissao = total_vendas * 0.15
salario_total = salario_fixo + comissao

print("O salário total de {} é: R$ {:.2f}".format(nome, salario_total))
    