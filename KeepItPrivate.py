class Private:
    __privatevariable = 27
    def __PrivateMethod(self):
        print("I'm inside my class")
    def hello(self):
        print("Value:", Private.__privatevariable)
randomvari = Private()
randomvari.hello()
randomvari.__PrivateMethod()