class Human:
    def __init__(self, n):
        self.name = n
        
    def print_name(self):
        print(self.name)
        return self.name
    
class Teacher(Human):
    def __init__(self, n):
        super().__init__(n)
        
    def print_name(self):
        print('teacher:', self.name)
    
a = Human('suhyeon')
b = Teacher('suhyeon')

a.print_name()
b.print_name()