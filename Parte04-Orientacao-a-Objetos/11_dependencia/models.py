class Calculadora:
    def somar(self,a,b):
        return a+b

    def subtrair(self,a,b):
        return a-b

    def multiplicar(self,a,b):
        return a*b

    def dividir(self,a,b):
        return a/b


class Pedido:
    def __init__(self, valor1, valor2):
        self.__valor1 = valor1
        self.__valor2 = valor2

    @property
    def valor1(self):
        return self.__valor1

    @valor1.setter
    def valor1(self,valor1):
        self.__valor1 = valor1

    @property
    def valor2(self):
        return self.__valor2

    @valor2.setter
    def valor2(self,valor2):
        self.__valor2 = valor2

    def calcular_total(self,operador):
        calc = Calculadora()
        match operador:
            case "1":
                return calc.somar(self.__valor1,self.__valor2)
            case "2":
                return calc.subtrair(self.__valor1,self.__valor2)
            case "3":
                return calc.multiplicar(self.__valor1,self.__valor2)
            case "4":
                return calc.dividir(self.__valor1,self.__valor2)
            case _:
                return "Operação inválida."