class Human:
    def __init__(self, n):
        self.name = n
        print('id=', id(self))
        
class Human:
    def __init__(self, n):
        self.name = n
    def print_name(self):
        print(self.name)
        return self.name

a = Human('su-hyeon Jang')
print(a.name)

a.print_name()

current_name = a.print_name()

current_name

new_name = Human.print_name(a)

b = Human('xxxx')
c = Human('xxxx')
b == c # False
b is c # b와 c가 완전히 같은가? # False

a = int(7)
b = int(7)
a == b # True
a is b # True

b = int(798472323)
a = int(798472323)
a is b # false # 미리 예측하지 못한 값이여서
a == b # True

class Student(Human):
    def __init__(self):
        super().__init__('not defined')
        
b = Student()
b.print_name() # not defined


a = Human() # error

class Teacher(Human):
    def __init__(self, n):
        super().__init__(n)
    def print_name(self):
        print('teacher:', self.n)
    
a = Human('suhyeon')
b = Tearcher('suhyeon')

a