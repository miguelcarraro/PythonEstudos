class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

aluno_1 = Estudante("Miguel", 1)
aluno_2 = Estudante("Kevilyn", 2)
mostrar_valores(aluno_1, aluno_2)

aluno_1.matricula = 3
mostrar_valores(aluno_1,aluno_2)

Estudante.escola = "Python"
aluno_3 = Estudante("Vanessa",4)

mostrar_valores(aluno_1,aluno_2,aluno_3)