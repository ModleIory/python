class classTest:
    def __init__(self):
        print("this is test")
    @classmethod
    def class_method(cls):
        print("this is class method")
    @staticmethod
    def static_method():
        print("this is static method")

classTest.class_method()
classTest.static_method()
c = classTest()
c.class_method()
c.static_method()