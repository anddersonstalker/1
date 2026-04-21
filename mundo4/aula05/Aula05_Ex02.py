class ContaBancaria():
    """
Cria uma conta bancaria e permite realizar saques e depositos.
    """
    def __init__(self, id, nome, saldo):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"Conta {self.id} criada com sucesso com R${self.saldo:,.2f} de saldo.")


    def __str__(self):
        return f"A conta nº {self.id} de titular {self.titular} tem um saldo de R${self.saldo:,.2f}"
    
    
    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito de R${valor:,.2f} realizado com sucesso")


    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saque no valor de R${valor:,.2f} NEGADO: SALDO INSUFICIENTE NA CONTA {self.id}.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} realizado com sucesso.")


c1 = ContaBancaria(112, 'Pedro', 3000)
c1.depositar(500)
c1.sacar(5000)
print(c1)
print(c1.__doc__)