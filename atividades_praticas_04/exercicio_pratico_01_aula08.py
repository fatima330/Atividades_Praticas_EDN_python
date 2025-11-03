def calcular():

    while True:
        print("\n=== CALCULADORA ===")
        try:

            num1 = float(input('Digite o primeiro numero: '))
            operacao = input('Digite a opearação(+, -, *, /): ')
            num2 = float(input('Digite o segundo numero: '))

            if operacao == '+':
                resultado = num1 + num2
                print(f"O resultado é: {resultado}" )
                break
            elif operacao == '-':
                resultado = num1 - num2
                print(f"O resultado é: {resultado}" )
                break
            elif operacao == '*':
                resultado = num1 * num2
                print(f"O resultado é: {resultado}" )
                break
            elif operacao == '/':
                resultado = num1 / num2
                print(f"O resultado é: {resultado}" )
                break
            else:
                print('Operação Invalida Digite apenas +, -, *, /')
        
        except ValueError:
            print("entrada invalida")
        except ZeroDivisionError:
            print('Erro nao é possivel dividir por zero')


calcular()
    