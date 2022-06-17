#Arquivo inicial

from calc.operacoes import soma, sub, mult, div

menu="""
Operações: 
1 - Adição
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Sair
"""


while True:
    op = input(menu)

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    if op == "1":
        print(soma(num1, num2))
    elif op == "2":
        print(sub(num1, num2))
    elif op == "3":
        print(mult(num1, num2))
    elif op == "4":
        print(div(num1, num2))
    elif op == "5":
        print("Saindo...")
        break

