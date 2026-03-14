#criar um programa que o usuário utilize para adivinhar um número
#além disso, o programa utiliza a biblioteca colorama para adicionar cores aos prints (apenas para testes)
import random
import colorama

numero = random.randint(1,100)
tentativas = 10

while True:
    try:
        chute = int(input(colorama.Fore.BLACK + colorama.Back.WHITE + 'Digite um numero entre 1 e 100:'))
        print()
        colorama.init(True)
        if numero < chute:
            print(colorama.Fore.RED +'Numero muito alto.')
            tentativas -= 1
        elif numero > chute:
            print(colorama.Fore.RED +'Numero muito baixo.')
            tentativas -= 1
        elif numero == chute:
            print(colorama.Fore.GREEN +'Parabéns, você acertou o numero :)')
            break
        if tentativas == 0:
            print(colorama.Fore.RED + f'Você excedeu a quantidade de tentativas, o numero era {numero}')
            break
        print(colorama.Fore.YELLOW + f'Voce ainda tem {tentativas} tentativas')
        print()
    except ValueError:
        print(colorama.Fore.YELLOW + 'Por favor digite apenas numeros válidos')
        print()