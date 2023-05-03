"""
QUESTÃO 7.0
    dia_semana é True para dias na semana
    feriado é True nos feriados
    você pode ficar dormindo quando é feriado ou não é dia semana
    retorne True ou False conforme você vá dormir ou não
    """

print('{0} exercício 7.0 {0}'.format(5 * '='))


def dormir(dia_semana, feriado):
    if not dia_semana or feriado:
        return True
    else:
        return False


print(dormir(False, True))

"""
QUESTÃO 7.1
  temos dois alunos a e b
  a_sorri e b_sorri indicam se a e b sorriem
  temos problemas quando ambos estão sorrindo ou ambos não estão sorrindo
  retorne True quando houver problemas
  """

print('{0} exercício 7.1 {0}'.format(5 * '='))


def alunos_problema(a_sorri, b_sorri):
    if not a_sorri and not b_sorri or a_sorri and b_sorri:
        return True
    else:
        return False


print(alunos_problema(False, True))

"""
QUESTÃO 7.2
   dados dois números inteiros retorna sua soma
   porém se os números forem iguais retorna o dobro da soma
   soma_dobro(1, 2) -> 3
   soma_dobro(2, 2) -> 8
   """

print('{0} exercício 7.2 {0}'.format(5 * '='))


def soma_dobro(a, b):
    if a != b:
        return a + b
    else:
        return (a+b)*2


print(soma_dobro(2, 2))


"""
QUESTÃO 7.3
    dado um inteiro n retorna a diferença absoluta entre n e 21
    porém se o número for maior que 21 retorna o dobro da diferença absoluta
    diff21(19) -> 2
    diff21(25) -> 8
    dica: abs(x) retorna o valor absoluto de x
"""

print('{0} exercício 7.3 {0}'.format(5 * '='))


def diff21(n):
    if abs(n < 21):
        return 21-n
    else:
        return abs(21-n)*2


print(diff21(19))


"""
QUESTÃO 7.4
    temos um papagaio que fala alto
    hora é um parâmetro entre 0 e 23
    temos problemas se o papagaio estiver falando antes da 7 ou depois das 20
"""

print('{0} exercício 7.4 {0}'.format(5 * '='))


def papagaio(falando, hora):
    if falando and (hora < 7 or hora > 20):
        return True
    else:
        return False


print(papagaio(False, 21))

"""
QUESTÃO 7.5
dados dois inteiros a e b
retorna True se um dos dois é 10 ou a soma é 10
"""

print('{0} exercício 7.5 {0}'.format(5 * '='))


def dez(a, b):
    if a == 10 or b == 10 or a + b == 10:
        return True
    else:
        return False


print(dez(5, 5))


"""
QUESTÃO 7.6
    seja um inteiro n
    retorna True se a diferença absoluta entre n e 100 ou n e 200
    for menor ou igual a 10
    dista10(93) -> True
    dista10(90) -> True
    dista10(89) -> False
"""

print('{0} exercício 7.6 {0}'.format(5 * '='))


def dista10(n):
    if abs(n - 100) <= 10 or abs(n - 200) <= 10:
        return True
    else:
        return False


print(dista10(89))


"""
QUESTÃO 7.7
    seja uma string s e um inteiro n
    retorna uma nova string sem a posição n
    apaga('kitten', 1) -> 'ktten'
    apaga('kitten', 4) -> 'kittn'
"""

print('{0} exercício 7.7 {0}'.format(5 * '='))


def apaga(s, n):
    return s[:n] + s[n+1:]


print(apaga('kitten', 1))


"""
QUESTÃO 7.8
    seja uma string s
    se s tiver tamanho <= 1 retorna ela mesma
    caso contrário troca a primeira e última letra
    troca('code') -> 'eodc'
    troca('a') -> 'a'
    troca('ab') -> 'ba'
"""

print('{0} exercício 7.8 {0}'.format(5 * '='))


def troca(s):
    if len(s) <= 1:
        return s
    else:
        trocada = s[-1] + s[1:-1] + s[0]
        return trocada


print(troca('code'))

# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0


def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = ' Falhou.'
    else:
        prefixo = ' Passou.'
        acertos += 1
    print('%s Esperado: %s \tObtido: %s' % (prefixo, repr(esperado), repr(obtido)))


def main():
  print('Oba! Hoje vou ficar dormindo!')
  test(dormir(False, False), True)
  test(dormir(True, False), False)
  test(dormir(False, True), True)
  test(dormir(True, True), True)

  print ()
  print ('Alunos problema')
  test(alunos_problema(True, True), True)
  test(alunos_problema(False, False), True)
  test(alunos_problema(True, False), False)
  test(alunos_problema(False, True), False)

  print ()
  print ('Soma dobro')
  test(soma_dobro(1, 2), 3)
  test(soma_dobro(3, 2), 5)
  test(soma_dobro(2, 2), 8)
  test(soma_dobro(-1, 0), -1)
  test(soma_dobro(0, 0), 0)
  test(soma_dobro(0, 1), 1)

  print ()
  print ('Diff21')
  test(diff21(19), 2)
  test(diff21(10), 11)
  test(diff21(21), 0)
  test(diff21(22), 2)
  test(diff21(25), 8)
  test(diff21(30), 18)

  print ()
  print ('Papagaio')
  test(papagaio(True, 6), True)
  test(papagaio(True, 7), False)
  test(papagaio(False, 6), False)
  test(papagaio(True, 21), True)
  test(papagaio(False, 21), False) # essa
  test(papagaio(True, 23), True)
  test(papagaio(True, 20), False)

  print ()
  print ('Dez')
  test(dez(9, 10), True)
  test(dez(9, 9), False)
  test(dez(1, 9), True)
  test(dez(10, 1), True)
  test(dez(10, 10), True)
  test(dez(8, 2), True)
  test(dez(8, 3), False)
  test(dez(10, 42), True)
  test(dez(12, -2), True)

  print ()
  print ('Dista 10')
  test(dista10(93), True)
  test(dista10(90), True)
  test(dista10(89), False)
  test(dista10(110), True)
  test(dista10(111), False)
  test(dista10(121), False)
  test(dista10(0), False)
  test(dista10(5), False)
  test(dista10(191), True)
  test(dista10(189), False)
  test(dista10(190), True)
  test(dista10(200), True)
  test(dista10(210), True)
  test(dista10(211), False)
  test(dista10(290), False)

  print ()
  print ('Apaga')
  test(apaga('kitten', 1), 'ktten')
  test(apaga('kitten', 0), 'itten')
  test(apaga('kitten', 2), 'kiten')
  test(apaga('kitten', 4), 'kittn')
  test(apaga('Hi', 0), 'i')
  test(apaga('Hi', 1), 'H')
  test(apaga('code', 0), 'ode')
  test(apaga('code', 1), 'cde')
  test(apaga('code', 2), 'coe')
  test(apaga('code', 3), 'cod')
  test(apaga('chocolate', 8), 'chocolat')

  print ()
  print ('Troca letras')
  test(troca('code'), 'eodc')
  test(troca('a'), 'a')
  test(troca('ab'), 'ba')
  test(troca('abc'), 'cba')
  test(troca(''), '')
  test(troca('Chocolate'), 'ehocolatC')
  test(troca('nythoP'), 'Python')
  test(troca('hello'), 'oellh')



if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" %(total, acertos,
     total-acertos, float(acertos*10)/total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")

