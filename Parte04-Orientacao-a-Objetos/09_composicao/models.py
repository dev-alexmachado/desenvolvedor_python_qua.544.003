class Motor:
    def __init__(self,potencia):
        self.__potencia = potencia

    @property
    def potencia(self):
        return self.__potencia

    @potencia.setter
    def potencia(self,potencia):
        self.__potencia = potencia

    def info(self):
        return f"Motor de {self.__potencia} cv"

class Carro:
    def __init__(self,modelo,potencia):
        self.__modelo = modelo
        self.__motor = Motor(potencia)

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self,modelo):
        self.__modelo = modelo

    def detalhes(self):
        return f"Carro: {self.__modelo} | {self.__motor.info()}"