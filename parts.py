class Parte:

    def __init__(self, tipo_de_parte, nome, nacionalidade, estado_civil, profissao, cpf, residencia):
        self.tipo_de_parte = tipo_de_parte.upper()
        self.__nome = nome.title()
        self.__nacionalidade = nacionalidade.capitalize()
        self.__estado_civil = estado_civil.capitalize()
        self.__profissao = profissao
        self.__cpf = cpf
        self.__residencia = residencia.title()
        self.lista = [tipo_de_parte, nome, nacionalidade, estado_civil, profissao, cpf, residencia]

    def __str__(self):
        return f'{self.tipo_de_parte}, {self.__nome},{self.__nacionalidade}, {self.__estado_civil}, {self.__cpf}, {self.__residencia}'

    def __iter__(self):  # permite iteração com a lista
        return iter(self.lista)
