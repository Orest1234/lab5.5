import lab5 as code
import unittest

class TestProgramm(unittest.TestCase):
    def test_rec(self):
        n = list(input('Введіть n: '))
        k = 0
        sum = 0
        count = []
        for i in range(len(n)):
               i = int(n[k])
               sum += i
               count.append(i)
               k += 1
        min = sorted((n))[0]
        max = sorted((n))[len((n)) - 1]
        result = f'''
Сума його цифр: {sum}
Кількість його цифр: {len(count)}
Максимальне число: {max}
Мінімальне число: {min}
Глибина рекурсії: {k}
                '''
        print(result)
        return result
        result_test = code.rec(n)
        self.assertEqual(result_test,result)