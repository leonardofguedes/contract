"""
Locação
Object | Time | Fee | Place | Signature
"""

class Rules:
    def __init__(self, object, time, fee, place):
        self.__object = object
        self.__time = time
        self.__fee = fee
        self.__place = place



    def object(self):
        return f'OBJETO: As partes ajustam contrato de {self.__object}.'


    def time(self):
        return f"PRAZO: O tempo deste contrato é de {self.__time} anos."


    def fee(self):
        return f'MULTA: A multa por descumprimento deste contrato é R$ {self.__fee}.'


    def place(self):
        return f'FORO: O foro para resolução deste contrato é {self.__place}.'


    def __str__(self):
        return self.__object, self.__time, self.__fee, self.__place

class Rent(Rules):

    def __init__(self, object, time, fee, place):
        super().__init__(object,time, fee, place)


class Job(Rules):

    def __init__(self, object, time, fee, place):
        super().__init__(object,time, fee, place)


class Sell(Rules):

    def __init__(self, object, time, fee, place):
        super().__init__(object,time, fee, place)

