#Calculadora em Python

print("\n****************************Calculadora em Python****************************")

def add(x,y):
    return x + y

def subtr(x,y):
    return x - y

def multi(x,y):
    return x * y

def div(x,y):
    return x / y

print("Selecione o número da operação desejada: \n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

selecione = input("\nDigite sua opção (1/2/3/4) : ")

num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("\nDigite o segundo número: "))

if selecione == '1':
    print("\n")
    print(num1, "+", num2, "=", add(num1, num2))
    print("\n")
elif selecione == '2':
    print("\n")
    print(num1, "-", num2, "=", subtr(num1, num2))
    print("\n")
elif selecione == '3':
    print("\n")
    print(num1, "*", num2, "=", multi(num1, num2))
    print("\n")
elif selecione == '4':
    print("\n")
    print(num1, "/", num2, "=", div(num1, num2))
    print("\n")

else:
    print("\nOpção Inválida.")