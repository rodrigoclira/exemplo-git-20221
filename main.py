#Arquivo inicial

from calc.operacoes import soma, sub, mult, div, pot

menu="""
Operações: 
1 - Adição
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Potência
6 - Sair
"""

"/home/rcls/Documents/GitHub/exemplo-git-20221/img/wonderlay.jpg" #Caminho Absoluto
"./img/wonderlay.jpg" #Caminho Relativo

while True:
    op = input(menu)

    if op == "6":
        print("Saindo...")
        break

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
        print(pot(num1, num2))
