#jogo da adivinhação les go
import random

numero = random.randint(1,100)
print("==bem vindo ao jogo da adivinhação==\n\n")
vitoria = False
tentativas = 10
while not vitoria:

    chute = int(input("chute um numero\n"))
    tentativas -= 1
    if tentativas == 0:
        print(f"tetativas acabadas, o numero secreto era {numero}")
        break
    elif chute == numero:
        print(f"você acertou o numero secreto com {tentativas} restantes, YAY")
        vitoria = True
    elif chute > numero:
        print(f"o numero secreto é menor, {tentativas} restantes")
    elif chute < numero:
        print(f"o numero secreto e maior, {tentativas} restantes")