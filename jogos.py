import forca
import adivinhacao
def escolha_jogo():
    print("***************************************")
    print("Escolha o seu jogo!")
    print("***************************************")

    print("(1) Forca (2) Adivinhação")
    jogo = int(input())

    if(jogo==1):
        print("Iniciando o jogo da Forca")
        forca.jogar()
    elif(jogo==2):
        print("Iniciando o jogo da Adivinhação")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolha_jogo()

