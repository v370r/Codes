import MonkeyFetching as m
def monkey_f(self):
    print("Got a monkey here!")

obj = m.MyClass()
#m.MyClass.f = monkey_f #tweak here!
obj.f()
