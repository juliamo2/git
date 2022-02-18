class Dog:
    def __init__(self,breed,name,age,sex):
        self.breed = breed
        self.name = name
        self.age = age
        self.sex = sex
    def eat(self):
        print(self.name,"在吃")

d01 = Dog("拉布拉多","黑米",4,"母")
d01.eat()

list01 = [d01,Dog("拉布拉多","白米",4,"母")]
def found():
    list_result = []
    for item in list01:
       if item.name == "白米":
           list_result.append(item)
    return list_result
