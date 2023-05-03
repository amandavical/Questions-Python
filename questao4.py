import unittest

"""
QUESTÃO 4.0
Dado um a lista de números, retorna uma lista onde
todo elemento adjacente e repetido será deletado reduzindo a um único elemento.
Então, [1, 2, 2, 3] retornará [1, 2, 3]
Você pode criar uma nova lista ou modificar a lista atual.
def remove_adjacent(nums):
    pass
"""

print('{0} exercício 4.0 {0}'.format(5 * '='))


def remove_adjacent(nums):
    # Cria uma lista vazia para armazenar o resultado
    result = []

    # Itera sobre a lista de números
    for num in nums:
        # Se o resultado estiver vazio ou o último número do resultado for diferente de num,
        # adiciona num ao resultado
        if len(result) == 0 or result[-1] != num:
            result.append(num)

    return result


print(remove_adjacent([1, 2, 2, 3]))

"""
QUESTÃO 4.1
Dado duas listas ordenadas em ordem crescente, criar e retornar uma
lista de todos os elementos em ordem algabética.
Você pode modificar as listas passadas.
Idealmente, a solução deve trabalhar em tempo "linear", 
que passa uma única vez em ambas as listas.
def linear_merge(list1, list2):
    pass
"""

print('{0} exercício 4.1 {0}'.format(5 * '='))


def linear_merge(list1, list2):
    # Cria uma lista vazia para armazenar o resultado
    result = []

    # Enquanto ambas as listas não estiverem vazias
    while len(list1) > 0 and len(list2) > 0:
        # Se o primeiro elemento de list1 vier antes do primeiro elemento de list2 na ordem alfabética,
        # remove e adiciona esse elemento ao resultado
        if list1[0] < list2[0]:
            result.append(list1.pop(0))
        # Caso contrário, remove e adiciona o primeiro elemento de list2 ao resultado
        else:
            result.append(list2.pop(0))

    # Adiciona o restante dos elementos de list1 e list2 ao resultado (se houver algum)
    result.extend(list1)
    result.extend(list2)

    return result


print(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']))


class MyTest(unittest.TestCase):
    def test_remove_adjacent(self):
        self.assertEqual(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
        self.assertEqual(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
        # Repare que são excluídos apenas os valores repetidos e adjacentes
        self.assertEqual(remove_adjacent([1, 2, 3, 2, 3]), [1, 2, 3, 2, 3])
        self.assertEqual(remove_adjacent([]), [])

    def test_linear_merge(self):
        self.assertEqual(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']), ['aa', 'bb', 'cc', 'xx', 'zz'])
        self.assertEqual(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']), ['aa', 'bb', 'cc', 'xx', 'zz'])
        self.assertEqual(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']), ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
    unittest.main()
