class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if value>=0 and value<=100 and isinstance(value, int):
            self._score = value

        else:
            print('输入成绩有误！')

s = Student()
s.score = 80
print(s.score)
s.score = 105
print(s.score)