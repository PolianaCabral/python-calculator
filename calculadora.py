n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

operacao = input("Escolha a operação (+, -, *, /): ")

if operacao == "+":
    print("Resultado:", n1 + n2)

elif operacao == "-":
    print("Resultado:", n1 - n2)

elif operacao == "*":
    print("Resultado:", n1 * n2)

elif operacao == "/":
    if n2 == 0:
        print("Não é possível dividir por zero")
    else:
        print("Resultado:", n1 / n2)

else:
    print("Operação inválida")
