from endereco import endereco
from pessoa import pessoa


class funcionario(pessoa):
    def __init__(self):
        self.matricula = ''
        self.email = ''
        self.e = endereco()

    def cadastrarFucionario(self):      
        self.matricula = input('Matrícula: ')
        self.cadastrarPessoa()
        self.email = input('Email: ')
        self.e.cadastrarEndereco()

    def listarFuncionario(self):     
        print('Matrícula:', self.matricula)
        self.listarPessoa()
        print('Email:', self.email)
        self.e.listarEndereco()


Joselito = funcionario()
Joselito.cadastrarFucionario()
Joselito.listarFuncionario()
