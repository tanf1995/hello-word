class Fib(object):
    def __init__(self, limit_value=0):
        self.__a = 0
        self.__b = 1
        self.limit_value = limit_value

    def __iter__(self):
        return self

    def __next__(self):
        self.__a, self.__b = self.__b, self.__a + self.__b
        if self.__a > self.limit_value:
            raise StopIteration()
        return self.__a

    # 可取第几项的值
    def __getitem__(self, item):
        self.__a, self.__b = 0, 1
        if isinstance(item, int):
            for i in range(item+1):
                self.__a, self.__b = self.__b, self.__a + self.__b
            return self.__a

        elif isinstance(item, slice):
            start = item.start
            stop = item.stop
            res = []
            for i in range(stop):
                self.__a, self.__b = self.__b, self.__a + self.__b
                if i >= start:
                    res.append(self.__a)
            return res

        else:
            print('索引错误！')


print('斐波那契数列')
value = int(input('最大限制值：'))
for i in Fib(value):
    print(i, end='--')

print('')
f = Fib()
print(f[5])
print(f[0:8])
