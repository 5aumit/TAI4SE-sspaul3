#the method of same name present in any class, it is call by anywhere
#object of different type is responds to same methods
class pycharm:
    def execute(self):
        print("COde check")
        print("compile")
class MyEditor:
    def execute(self):
        print("Spell Cheack")
        print("Auto COmpile")
        print("COde check")
        print("compile")


class laptop:
    def code(self,ide):
        ide.execute()

ide=pycharm()
ide2=MyEditor()
a1=laptop()
a1.code(ide)
print()
a1.code(ide2)

