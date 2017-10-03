class Screen(object):
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def resolution(self):
        return self.width*self.height

# test:
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
# 测试结果如果不等于正确数值，报异常
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution