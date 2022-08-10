import jogo_de_forca
import jogo_da_adivinhacao

def escolha():
    print("--------------------------------")
    print("*******Escolha seu Jogo!********")
    print("--------------------------------")

    print("(1) Forca - (2) Adivinhação")

    jogo = int(input("Qual jogo você quer jogar? "))

    if(jogo == 1):
        print("Você escolheu jogo da Forca.")
        jogo_de_forca.jogar()
    elif(jogo == 2):
        print("Você escolheu o jogo da adivinhação.")
        jogo_da_adivinhacao.jogar()

if (__name__ == "__main__"):
    escolha()
