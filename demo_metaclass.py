def constructeur(self, *args, **kwargs):
    self.arguments = args
    self.keywords_arguments = kwargs

class MyMetaClass(type):
    def __new__(cls, clsname, superclasses, attributedict):
        print(cls)
        print(clsname)
        print(superclasses)
        print(attributedict)
        if '__init__'not in attributedict:
            attributedict['__init__'] = constructeur
        return super().__new__(cls, clsname, superclasses, attributedict)


class MyClass(metaclass=MyMetaClass):
    URL = 'https://randomuser.me/api'

instance = MyClass('ddddd', 'eeeee')
print (vars(instance))