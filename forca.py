import random



def jogar(): #função

    imprime_mensagem_abertura()

    palavra_secreta=carrega_palavra_secreta()

    letras_acertadas = [] #criando uma lista vazia

    letras_acertadas=inicializa_letras_acertadas(palavra_secreta)

    enforcou= False
    acertou = False
    erros = 0

    print(letras_acertadas)
    while(not enforcou and not  acertou):
        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute,letras_acertadas,palavra_secreta)
        else:
            erros = erros +1
            desenha_forca(erros)

        enforcou = erros ==7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)



    print("***********Fim do jogo!***********")




def imprime_mensagem_abertura():
    print("***************************************")
    print("Bem vindo ao jogo da forca")
    print("***************************************")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")  # abrindo o arquivo de palavras
    palavras = []  # criando uma lista para pegar as palavras do arquivo

    for linha in arquivo:
        linha = linha.strip() # essa função retira os espaços e os \n no final da palavra
        palavras.append(linha) #essa função adiciona a palavra no final da lista
    arquivo.close()
    numero=random.randrange(0,len(palavras)) #gerando um número aleatório para usarmos como indice na lista
    palavra_secreta = palavras[numero].upper() #atribuo a palavra secreta a palavra da lista na posição gerada
    return palavra_secreta

def inicializa_letras_acertadas(palavra_secreta):
    return["_" for letra in palavra_secreta] #colocando o caracter _ dentro da lista

def pede_chute():
    chute=input("Qual letra?")
    chute = chute.strip().upper()  # removendo espaço antes e depois da letra #sempre comparando em letra maiuscula
    return chute

def marca_chute_correto(chute,letras_acertadas,palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):  # sempre comparando em letra maiuscula
            letras_acertadas[index] = letra
        index = index + 1

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


if(__name__ == "__main__"): #utilizamos essa condição para chamar a própria função aqui desse código
    jogar() #utilizamos essa condição para chamar a própria função aqui desse código