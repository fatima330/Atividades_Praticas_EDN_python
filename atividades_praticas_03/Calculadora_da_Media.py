num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
num4 = float(input("Digite o quarto número: "))

media = (num1*2 + num2*3 + num3*4 + num4*1) / (2+3+4+1)
print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado !!: {:.2f}".format(media))
elif media < 5.0:
    print("Aluno reprovado !! : {:.2f}".format(media))
else:
    print("Aluno em exame !!")
    
    nota_exame = float(input("Digite a nota do exame: "))
    print(f"Nota do exame: {nota_exame:.1f}")

    media_final = (media + nota_exame) / 2

    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    
    print(f"Media final: {media_final:.1f}")