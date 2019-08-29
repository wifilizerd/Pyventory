class Emplyee:
    def __init__(self):
       pass

    def fullName (self, first = "default", last = "nothing"):
        self.first = first
        self.last = last
        print('{} {}'.format(self.first, self.last))
        self.first = input('first:')
        self.last = input('last:')
        return('{} {}'.format(self.first, self.last))
    
emp_1 = Emplyee()
emp_2 = Emplyee()

# print(emp_1.first)
# print(emp_2.first)
# print(emp_2.fullName())

print(emp_1.fullName())




