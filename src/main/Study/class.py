
'''
class Service:
    says = 'I dont know'
    def __init__(self, name):
        self.name = name
    def sum(self, a, b):
        result = a + b
        print('%s %s + %s =  %s' % (self.name, a, b, result))


add = Service('Nick')
add.sum(1, 1)
'''
'''
class 클래스이름[(상속 클래스명)]:
    <클래스 변수 1>
    <클래스 변수 2>
    ...
    def 클래스함수1(self[, 인수1, 인수2,,,]):
        <수행할 문장 1>
        <수행할 문장 2>
        ...
    def 클래스함수2(self[, 인수1, 인수2,,,]):
        <수행할 문장1>
        <수행할 문장2>
'''
class Fourcal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def sum(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result

a = Fourcal()
b = Fourcal()
a.setdata(4, 2)
b.setdata(3, 7)
a.sum()
a.mul()
a.sub()
a.div()
b.sum()
b.mul()
b.sub()
b.div()