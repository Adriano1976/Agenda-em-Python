class endereco:
    def __init__(self):
        self.logradouro = ''
        self.numero = ''
        self.complemento = ''
        self.bairro = ''
        self.cidade = ''
        self.uf = ''
        self.cep = ''

    def cadastrarEndereco(self):
        self.logradouro = input('Endereço: ')
        self.numero = input('Número: ')
        self.complemento = input('Complemento: ')
        self.bairro = input('Bairro: ')
        self.cidade = input('Cidade: ')
        self.uf = input('UF: ')
        self.cep = input('CEP: ')

    def listarEndereco(self):
        print('Logradouro:', self.logradouro)
        print('Nª:', self.numero)
        print('Complemento:', self.complemento)
        print('Bairro:', self.bairro)
        print('Cidade:', self.cidade)
        print('UF:', self.uf)
        print('Cep:', self.cep)
