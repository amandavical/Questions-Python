"""
QUESTÃO 2.0
Dado uma string, procurar a primeira ocorrência da substring 'not' e 'bad'
Se 'bad' vier após o 'not'
substituir todo o trecho "not ... bad" por 'good'
Retorne a string resultante.
def not_bad(s):
    #SEU CODIGO AQUI
    pass
"""
import unittest

print('{0} exercício 2.0 {0}'.format(5 * '='))


def not_bad(s):
    not1 = s.find('not')
    bad2 = s.find('bad')
    if not1 != -1 and bad2 != -1 and bad2 > not1:
        return s[:not1] + 'good' + s[bad2 + 3:]
    else:
        return s


print(not_bad('it is not bad for me'))

"""
QUESTÃO 2.1
Considere dividir uma string em duas metades.
Se o comprimento for par, a parte da frete (front) e a parte de trás (back) são do mesmo tamanho.
e o comprimento for ímpar, o caracter extra irá para a parte da frente.
"""

print('{0} exercício 2.1 {0}'.format(5 * '='))


def splice(s):
    length = len(s)
    if length % 2 == 0:
        front = s[:length // 2]
        back = s[length // 2:]
    else:
        front = s[:length // 2 + 1]
        back = s[length // 2 + 1:]
    return front, back


print(splice('amarelo'))

"""
QUESTÃO 2.2 
Dado 2 strings, 'a' e 'b', retornar um string na forma
a front + b front + a back + b back
def front_back(a, b):
    #SEU CODIGO AQUI
    pass
"""

print('{0} exercício 2.2 {0}'.format(5 * '='))


def front_back(a, b):
    front_a = a[:len(a) // 2 + len(a) % 2]  # impar +1 e par +0
    front_b = b[:len(b) // 2 + len(b) % 2]
    back_a = a[len(a) // 2 + len(a) % 2:]
    back_b = b[len(b) // 2 + len(b) % 2:]

    return front_a + front_b + back_a + back_b


print(front_back('abcde', 'xyz'))


class MyTest(unittest.TestCase):

    def test_not_bad(self):
        self.assertEqual(not_bad('This movie is not so bad'), 'This movie is good')
        self.assertEqual(not_bad('This dinner is not that bad!'), 'This dinner is good!')
        self.assertEqual(not_bad('This tea is not hot'), 'This tea is not hot')
        self.assertEqual(not_bad("It's bad yet not"), "It's bad yet not")

    def test_front_back(self):
        self.assertEqual(front_back('abcd', 'xy'), 'abxcdy')
        self.assertEqual(front_back('abcde', 'xyz'), 'abcxydez')
        self.assertEqual(front_back('Kitten', 'Donut'), 'KitDontenut')


if __name__ == '__main__':
    unittest.main()
