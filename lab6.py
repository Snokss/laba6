def add_sizer(a):

def sizer(self):
self.size = self.a

if len(str(abs(self.size))) != 1:
return len(str(self.size))
elif type(abs(self.size)) == int or type(abs(self.size)) == float:
return abs(self.size)
else:
return 0

a.sizer = sizer
return a

@add_sizer
class MyClass:
def __init__(self, a):
self.a = a

my_obj = MyClass(14)
print(my_obj.sizer())