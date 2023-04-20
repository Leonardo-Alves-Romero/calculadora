def calculadora():
    # Definindo as operaçoes matematicas da calculadora 
    operacoes = ['+', '-', '*', '/']

    # Pedindo para o úsuario dar os números  e sinal aritmético que serão usados na conta
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = (input("Digite a operação que deseja realizar (+,-,*,/) : "))

    # Realizando as contas com os respectivos sinais aritméticos
    if operacao == "+":
        resultado = num1 + num2
    
    elif operacao == "-":
        resultado = num1 - num2

    elif operacao == "*":
        resultado = num1 * num2

    elif operacao == "/":
        # Caso úsuario tente fazer uma divisão por zero
        if num2 ==0:
            print('Não é possível dividir por 0, tente novamente!!')
            return
        resultado = num1 / num2

    print("O resultado da operação é: ", resultado)

calculadora()