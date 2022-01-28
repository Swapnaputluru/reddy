# private variables only access with in the class

class Family:
    __mother = "laxmi"
    __father = "reddy"
    __brother = "hanu"
    __sister = "paddu"

    def hide(self):
        print(self.__mother,self.__father,self.__brother,self.__sister)


f1 = Family()
f1.hide()

# print(Family.__mother)  AttributeError: type object 'family' has no attribute '__mother'
#  we can't access because that is private variable

print("------------------private method-----------------")


class hiding:
    def __personal(self):
        print("hiding personal details")

    def proffessional(self):
        print("no need to hide details")

h1 = hiding()
h1.proffessional()
# h1.__personal()   AttributeError: 'hiding' object has no attribute '__personal' ,because this is private method

# indirectly change the private variable value

class variable:
    number = 23
    def num(self,numb):
        self.number = numb
        print(numb)

    def value(self):
        print(self.number)

print("----------------given private variable value------------------")
obj = variable()
obj.value()
print("----------------after changing value------------------")
obj.num(21)
obj.value()
