from abc import ABC, abstractmethod

class Class1(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def method1(self):
        pass
    
    def method5(self):
        pass

    def list_parent_methods(self):
        bases = self.__class__.__bases__
        if not bases:
            return {"parent_class": None, "methods": []}

        parent = bases[0]  # Immediate parent class
        method_names = [name for name in vars(parent)
                        if callable(getattr(parent, name)) and not name.startswith("__")]

        return {"parent_class": parent.__name__, "methods": method_names}


class Class2(Class1):
    def __init__(self):
        super().__init__()

    def method1(self):
        return "this is overriden"

    def method2(self):
        pass

    def method3(self):
        pass

class Class3(Class2):
    def __init__(self):
        super().__init__()

    def method4(self):
        pass


m = Class2()
print(m.list_parent_methods())

m2 = Class3()
print(m2.list_parent_methods())

print(m2.method5())

