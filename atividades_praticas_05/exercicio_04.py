from datetime import date

def idade_em_dias(ano_nascimento: int) -> int:

    ano_atual = date.today().year  
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365 
    return idade_dias


ano = int(input("Digite o ano de nascimento: "))
print(f"Você tem aproximadamente {idade_em_dias(ano)} dias de idade.")
