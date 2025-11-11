import string

def verificar_palindromo(texto: str) -> str:
    
    texto_limpo = ''.join(
        caractere.lower()
        for caractere in texto
        if caractere.isalnum() 
    )

    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"


print(verificar_palindromo("Ame a ema"))        # Sim
print(verificar_palindromo("Socorram-me subi no ônibus em Marrocos"))  # Sim
print(verificar_palindromo("Python"))           # Não
