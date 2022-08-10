import random

def jogar():

    print("--------------------------------")
    print("Bem vindo ao jogo da adivinhação")
    print("--------------------------------")

    numero_secreto = round(random.randrange(1,101))
    pontos = 1000

    print("QUal nível de dificuldade?")
    print("(1) Fácil - (2) Médio - (3) Difícil")

    nivel = int(input("Qual nível quer jogar? "))

    if (nivel == 1):
        tentativas = 10
    elif (nivel == 2):
        tentativas = 5
    else:
        tentativas = 3

    for rodada in range(1, tentativas+1):
        print("Tentativa {} de {}".format(rodada, tentativas))
        chute_input = input("Digite um Número entre 1 e 100: ")
        chute = int(chute_input)

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        print("Você digitou ", chute_input)

        if (acertou):
            print("Você acertou e fez {} pontos.".format(pontos))
            break
        else:
            if (maior):
                print("Você errou, o seu palpite foi maior que o número!")
            elif (menor):
                print("Você errou! seu palpite foi menor que o número!")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos



    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()
