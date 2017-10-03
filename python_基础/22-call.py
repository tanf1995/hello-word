class Task(object):
    def __init__(self, name):
        self.__name = name

    def __call__(self, *args, **kwargs):
        print(args)
        print('穿入参：%s'%args)
        print('任务名：%s'%self.__name)

t1 = Task('t1')
t1('hello')