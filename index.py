class myClass():
    __privatevar__ = 27
    def __priveMeth(self):
        print("Im inside class myclass")
    def hello(self):
        print(f"Private variable value: {myClass.__privatevar__}")

fo = myClass()
fo.hello()
fo.__priveMeth()