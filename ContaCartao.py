from datetime import datetime
import pytz
from random import randint

class ContaCorrente:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone("Brazil/East")
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')


    def __init__(self,nome, cpf, agencia, NumConta):
        self._nome = nome
        self._cpf = cpf
        self._agencia = agencia
        self._numconta = NumConta
        self._saldo = 0
        self._limite = None
        self._transacoes = []
        self._cartoes = []

    def consultar_saldo(self):
        print('Seu saldo atual é de : R${:,.2f}' .format(self.saldo))

    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append((f'Deposito: {valor}', f'Saldo atual: {self.saldo}', ContaCorrente._data_hora()))

    def _limite_conta(self):
        self.limite = -1000
        return self.limite

    def sacar(self,valor):
        if self.saldo - valor < self._limite_conta():
            print('Você não tem saldo suficiente para o saque')
        else:
            self.saldo -= valor
            self.transacoes.append((f'Saque: {valor}', f'Saldo atual: {self.saldo}', ContaCorrente._data_hora()))

    def consultar_historico(self):
        print('Histórico de transações: ')
        for transacao in self.transacoes:
            print(transacao)

    def transferencia(self, valor, conta_destino):
        self.sacar(valor)
        conta_destino.saldo += valor
        conta_destino.transacoes.append((f'Deposito: {valor}', f'Saldo atual: {conta_destino.saldo}', ContaCorrente._data_hora()))


class CartaoCredito:


    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone("Brazil/East")
        horario_BR = datetime.now(fuso_BR)
        return horario_BR

    def __init__(self, titular, conta_corrente):
        self.nome = titular
        self.numero = randint(1000000000000000, 9999999999999999)
        self.validade = '{}/{}' .format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4)
        self.CVS = '{}{}{}'.format(randint(0, 9),randint(0, 9),randint(0, 9))
        self.limite = None
        self.conta_corrente = conta_corrente
        conta_corrente._cartoes.append(self)

