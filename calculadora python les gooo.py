#calculadora python les gooo

operacoes = ["somar", "subtrair", "multiplicar", "dividir"]

#operações

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir (a, b):
    if b == 0:
        return "ta tentando dividir por zero seu bostinha?"
    return a / b

#guarda os números

print("bem vindo a estupida calculadora de maicon(bem estupida mesmo)")
num1 = int(input("por favor digite o primeiro numero\n"))
num2 = int(input("por favor digite o segundo numero\n"))

#operador em ação
while True:
    operador = input(f"agora escolha sua operacao:\n{operacoes}\n")
    if operador not in operacoes:
        print("\noperacao inválida\n")
    
    elif operador == "somar":
        print("resultado =", somar(num1, num2))
        break
    elif operador == "subtrair":
        print("resulado =", subtrair(num1, num2))
        break
    elif operador == "multiplicar":
        print("resultado =", multiplicar(num1, num2))
        break
    elif operador == "dividir":
        print("resultado =", dividir(num1, num2))
        break