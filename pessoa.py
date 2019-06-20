class pessoa:
    nome = ''
    cpf = ''
    rg = ''

    def cadastrarPessoa(self):
        self.nome = input('Nome: ')
        self.cpf = input('CPF: ')
        self.rg = input('RG: ')

    def listarPessoa(self):
        print ('Nome:',self.nome)
        print ('CPF:',self.cpf)
        print ('RG:',self.rg)
