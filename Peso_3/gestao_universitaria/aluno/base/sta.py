from Peso_3.gestao_universitaria.aluno.base.funcionario import Funcionario


class STA(Funcionario):

    def __init__(self, cpf: str, nome: str, nivel: int):
        self.cpf = cpf
        self.nome = nome
        self.nivel = nivel