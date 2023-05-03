# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import unittest

"""
QUESTÃO 1.0
Dado um `count` como sendo o números de donuts, 
retornar uma string na forma "Número de donuts: <count>",
caso `count` seja maior ou igual a 10 retornar "many".
"""

print('{0} exercício 1.0 {0}'.format(5 * '='))


def donuts(count):
    if count >= 10:
        return "Number of donuts: many"
    else:
        return "Number of donuts: " + str(count)


print(donuts(5))

"""
QUESTÃO 1.1
Dado uma string qualquer `s`, retonar uma string
composta dos 2 primeiros e os 2 últimos caracteres, exemplo:
panela ----> pala
bala   ----> bala
mao    ----> maao
ja     ----> jaja

Caso a string `s` contenha menos que 2 caracteres,
retornar "" (string de cumprimento zero).
def both_ends(s):
    pass
"""

print('{0} exercício 1.1 {0}'.format(5 * '='))


def both_ends(s):
    if len(s) < 2:
        return ""
    else:
        return s[0:2] + s[-2:]


print(both_ends('panela'))

"""
QUESTÃO 1.2
Dado uma string `s`, retornar uma string onde
todas as ocorrências de seu primeiro caractere
seja alterado para '*', exceto o primeiro caracter. Exemplo:
babble ---> ba**le
Presuma que o tamanho da string seja 1 ou mais.
Dica: s.replace (strA, strB) retorna uma versão da string s
def fix_start(s):
    pass
"""

print('{0} exercício 1.2 {0}'.format(5 * '='))


def fix_start(s):
    first_char = s[0]
    modified = s[1:].replace(first_char, '*')
    return first_char + modified


print(fix_start('brabo'))

"""
Dado duas string `a` e `b`,  trocar os 2 primeiros caracteres entre as variáveis
e retornar uma única string separada por espaço como no exemplo:
"pezzy", "firm" ----> "fizzy perm"
def mix_up(a, b):
    pass
"""

print('{0} exercício 1.3 {0}'.format(5 * '='))


def mix_up(a, b):
    new_a = a.replace(a[:2], b[:2])
    new_b = b.replace(b[:2], a[:2])
    return new_a + " " + new_b


print(mix_up('pezzy', 'firm'))


class MyTest(unittest.TestCase):

    def test_donuts(self):
      self.assertEqual(donuts(4), 'Number of donuts: 4')
      self.assertEqual(donuts(9), 'Number of donuts: 9')
      self.assertEqual(donuts(10), 'Number of donuts: many')
      self.assertEqual(donuts(99), 'Number of donuts: many')

    def test_both_ends(self):
      self.assertEqual(both_ends('spring'), 'spng')
      self.assertEqual(both_ends('Hello'), 'Helo')
      self.assertEqual(both_ends('a'), '')
      self.assertEqual(both_ends('xyz'), 'xyyz')
      self.assertEqual(both_ends('xy'), 'xyxy')

    def test_fix_start(self):
      self.assertEqual(both_ends('xy'), 'xyxy')
      self.assertEqual(fix_start('babble'), 'ba**le')
      self.assertEqual(fix_start('aardvark'), 'a*rdv*rk')
      self.assertEqual(fix_start('google'), 'goo*le')
      self.assertEqual(fix_start('donut'), 'donut')

    def test_mix_up(self):
      self.assertEqual(mix_up('mix', 'pod'), 'pox mid')
      self.assertEqual(mix_up('dog', 'dinner'), 'dig donner')
      self.assertEqual(mix_up('gnash', 'sport'), 'spash gnort')
      self.assertEqual(mix_up('pezzy', 'firm'), 'fizzy perm')


if __name__=="__main__":
    #Questão 1
    unittest.main()


