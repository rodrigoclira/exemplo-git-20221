#Arquivo inicial

#Autor: Alderi


def soma(num1,num2):
    sub("Operação de Adição")
    resultado = num1+num2
    return resultado


def sub(num1,num2):
    sub("Operação de Subtração")
    resultado = num1-num2
    return resultado


def mult(num1=1, num2=2):
    return num1 * num2

def div(num1=6, num2=6):
    if num2 == 0:
        return "Não é possível divisão por Zero"
    else:
        return num1 / num2
    
        
