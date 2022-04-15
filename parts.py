class Parte:
    number = 0

    def __init__(self, tipo_de_parte, nome, nacionalidade, estado_civil, profissao, cpf, residencia):
        self.tipo_de_parte = tipo_de_parte.upper()
        self.__nome = nome.title()
        self.__nacionalidade = nacionalidade.capitalize()
        self.__estado_civil = estado_civil.capitalize()
        self.__profissao = profissao
        self.__cpf = cpf
        self.__residencia = residencia.title()
        Parte.number += 1

    def __str__(self):
        return self.tipo_de_parte, self.__nome, self.__nacionalidade, self.__estado_civil, self.__cpf, self.__residencia

    @classmethod
    def number_of_parts(self):
        return print(f'Este documento possui {Parte.number} participante(s).')

    @property
    def qualific(self): #qualificação
        return (f'{self.tipo_de_parte}: {self.__nome}, {self.__estado_civil},'
                     f' {self.__nacionalidade}, CPF com nr: {self.__cpf},'
                     f' residente em {self.__residencia}.')




