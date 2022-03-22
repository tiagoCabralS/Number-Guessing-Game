def linha(tam=42):
    print('-' * tam)


def cabecalho(txt):
    linha()
    print(f'{txt:^42}')
    linha()


def explicação():
    print('O que é o jogo de adivinhação de números?')
    print('\nO jogo de adivinhação de números, é um jogo simples de adivinhação,\n'
          'onde o usuário deve adivinhar um número entre 0 e N números de acordo com a fase.'
          '\nO jogo irá acabar depois de 10 tentativas para 5 fases, cada uma ficando mais difícil,'
          '\nse o jogador falhar em adivinhar o número em qualquer fase, o jogo será finalizado.')
