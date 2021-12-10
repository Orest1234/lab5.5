def rec(n,sum=0,count=[],k = 0):
    if k == len((n)):
        min = sorted((n))[0]
        max = sorted((n))[len((n))-1]
        result = f'''
Сума його цифр: {sum}
Кількість його цифр: {len(count)}
Максимальне число: {max}
Мінімальне число: {min}
Глибина рекурсії: {k}
        '''
        print(result)
        return result
    else:
        i = int(n[k])
        sum += i
        count.append(i)
        k += 1
        return rec(n,sum,count,k)


def main():
    n =  list(input('Введіть n: '))
    res = rec(n)
main()
