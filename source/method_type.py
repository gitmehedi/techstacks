# Instance Methods

class InstanceMethod:
    instanceName=None

    def setName(self,name):
        self.instanceName = name

    def getName(self):
        return self.instanceName
    

ins = InstanceMethod()
ins.setName('Mehedi Hasan')
result = ins.getName()
print(result)


# Class Methods

class ClassMethod:
    className = "Class Mehedi"

    @classmethod
    def getClassName(cls):
        return cls.className
    
result = ClassMethod.getClassName()
print(result)


# Static Methods

class StaticMethod:
    staticName = "Static Mehedi"

    @staticmethod
    def utility():
        return "This is a static method"
    
s1
