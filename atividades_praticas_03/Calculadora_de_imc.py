peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do peso") 
elif imc >= 25:
    print("Peso normal")
elif imc >= 30:
    print("Sobrepeso")
elif imc >= 35:
    print("Obeso")