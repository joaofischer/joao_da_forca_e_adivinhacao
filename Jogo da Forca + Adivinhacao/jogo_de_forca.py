import random


def jogar():

    mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    
    palavra_lista = inicializa_lista_letras(palavra_secreta)
    print(palavra_lista)

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):

        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, palavra_lista, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)
            #print("Tentativa {} de 10".format(erros))

        print(palavra_lista)

        enforcou = erros == 7
        acertou = '_' not in palavra_lista

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim de Jogo!")


def mensagem_abertura():
    print("--------------------------------")
    print("Bem vindo ao jogo da forca!")
    print("--------------------------------")


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    palavra_random = random.randrange(0, len(palavras))

    palavra_secreta = palavras[palavra_random].upper()

    return palavra_secreta


def inicializa_lista_letras(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(chute, palavra_lista, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            palavra_lista[index] = letra
        index += 1

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == "__main__"):
    jogar()
