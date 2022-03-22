def leiaInt(msg):
    n = ''
    ok = False
    while not ok:
        try:
            n = str(input(f'{msg}'))
            n = int(n)
            ok = True
        except:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
    return n


def fase(maxi, ultima=False):
    from random import randint
    from math import trunc
    comp = randint(0, maxi)
    tenta = trunc(maxi/2)
    print(f'Foi sorteado um número entre \033[1;36m0\033[m e \033[1;36m{maxi}\033[m, Você tem \033[1;35m{tenta}\033[m tentativas.')
    for c in range(0, tenta):
        esc = leiaInt('Seu palpite-> ')
        if esc == comp:
            if not ultima:
                print('\033[32mVocê acertou o número! Pode ir para próxima fase.\033[m')
            else:
                print('\033[32mO jogo acabou, voê consegui adivinhar todos os números. Parabéns.\033[m')
            return True
        if c == tenta and esc != comp:
            return False
        elif c != tenta and esc < comp:
            print('\033[31mPalpite muito baixo! Chute mais alto.\033[m')
        elif c != tenta and esc > comp:
            print('\033[31mPalpite muito alto! Chute mais baixo.\033[m')
