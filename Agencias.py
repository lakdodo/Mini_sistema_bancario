class Agencia:

    def __init__(self, telefone, numero, codigo):
        self.telefone = telefone
        self.numero = numero
        self.codigo = codigo
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('O caixa está com um valor abaixo do recomendado. Caixa atual: R${:,.2f}' .format(self.caixa))
        else:
            print('O caixa atual é: R${:,.2f}' .format(self.caixa))

    def realizar_emprestimo(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Empréstimo não é possível. Excede o caixa.')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome,cpf,patrimonio))


class AgenciaVirtual(Agencia):

    def __init__(self,site, telefone, numero, codigo):
        self.site = site
        super().__init__(telefone, numero, codigo)
        self.caixa = 1000000
        self.caixa_paypal = 0

    def depositar_paypal(self, valor):
        if self.caixa >= valor:
            self.caixa -= valor
            self.caixa += valor
        else:
            print('Não será possível realizar a transação. O valor excede o caixa.')

    def sacar_paypal(self,valor):
        if self.caixa_paypal >= valor:
            self.caixa_paypal -= valor
            self.caixa += valor
        else:
            print('Não será possível realizar a transação. O valor excede o caixa.')

class AgenciaNormal(Agencia):

    def __init__(self, telefone, numero, codigo):
        super().__init__(telefone, numero, codigo)


class AgenciaPremium(Agencia):

    def __init__(self, telefone, numero, codigo):
        super().__init__(telefone, numero, codigo)
        self.caixa = 10000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print('O cliente não possui patrimônio suficiente para entrar nesta agência.')

