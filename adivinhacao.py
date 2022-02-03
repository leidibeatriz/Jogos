import random

def jogar(): #função
    print("***************************************")
    print("Bem vindo ao jogo de adivinhação")
    print("***************************************")

    numero_secreto= random.randrange(1,101) #gerando número secreto aleatóriamente entre 1...100

    total_tentativas=0
    rodada=1
    pontos=1000

    nivel=int(input("Qual o nível de dificuldade você deseja?\n1-Fácil\n2-Médio\n3-Difícil\n"))

    #Definindo o nível do jogo, isso irá impactar na quantidade de tentativas:
    if(nivel==1):
        total_tentativas=20
    elif(nivel==2):
        total_tentativas=10
    else:
        total_tentativas=5

    for rodada in range(1, total_tentativas+1):
        print("Tentativa {} de {}".format(rodada,total_tentativas))
        chute = input("Digite um número entre 1 e 100: ") #input sempre retorna uma str

        print("Você digitou ", chute)

        numero=int(chute) #convertendo a variável chute em inteiro para comparar

        if(numero<1 or numero>100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        #testanto as condições e aplicando na variavél:
        acertou = numero == numero_secreto
        maior = numero > numero_secreto
        menor = numero < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
                if (rodada == total_tentativas):
                    print("Suas tentativas acabaram. O número secreto era {}, você fez {} pontos".format(numero_secreto,pontos))

            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
                if(rodada==total_tentativas+1):
                    print("Suas tentativas acabaram. O número secreto era {}, você fez {} pontos".format(numero_secreto,pontos))
            pontos_perdidos=abs(numero_secreto-numero)
            pontos=pontos - pontos_perdidos
        rodada=rodada+1

    print("***********Fim do jogo!***********")

if(__name__ == "__main__"): #utilizamos essa condição para chamar a própria função aqui desse código
    jogar() #utilizamos essa condição para chamar a própria função aqui desse código