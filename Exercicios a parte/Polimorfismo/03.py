from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, id_funcionario):
        self.__nome = nome
        self.__id_funcionario = id_funcionario

    @property
    def nome(self):
        return self.__nome

    @property
    def id_funcionario(self):
        return self.__id_funcionario
    
    @abstractmethod
    def calcular_pagamento(self):
        pass

    def __str__(self):
        return f"Nome: {self.nome}, ID: {self.id_funcionario}"


class FuncionarioMensal(Funcionario):
    def __init__(self, nome, id_funcionario, salario_mensal):
        super().__init__(nome, id_funcionario)
        self.salario_mensal = salario_mensal 

    @property
    def salario_mensal(self):
        return self.__salario_mensal
    
    @salario_mensal.setter
    def salario_mensal(self, novo_salario):
        if novo_salario >= 0:
            self.__salario_mensal = novo_salario
        else:
            print("Erro: O salário deve ser um valor positivo.")
    
    def calcular_pagamento(self):
        return self.salario_mensal


class FuncionarioHorista(Funcionario):
    def __init__(self, nome, id_funcionario, horas_trabalhadas, valor_hora):
        super().__init__(nome, id_funcionario)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    @property
    def horas_trabalhadas(self):
        return self.__horas_trabalhadas
    
    @horas_trabalhadas.setter
    def horas_trabalhadas(self, nova_hora):
        if nova_hora >= 0:
            self.__horas_trabalhadas = nova_hora
        else:
            print("Erro: A hora deve ser positiva!.")
    
    @property
    def valor_hora(self):
        return self.__valor_hora
    
    @valor_hora.setter
    def valor_hora(self, novo_valor):
        if novo_valor >= 0:
            self.__valor_hora = novo_valor
        else:
            print("O Valor deve ser positivo.")

    def calcular_pagamento(self):
        return self.horas_trabalhadas * self.valor_hora
    

class FuncionarioComissionado(FuncionarioMensal):
    def __init__(self, nome, id_funcionario, salario_mensal, comissao):
        super().__init__(nome, id_funcionario, salario_mensal)
        self.comissao = comissao

    @property
    def comissao(self):
        return self.__comissao
    
    @comissao.setter
    def comissao(self, nova_comissao):
        if nova_comissao >= 0:
            self.__comissao = nova_comissao
        else:
            print("Erro: Comissão não pode ser negativa!")

    def calcular_pagamento(self):
        salario_base = super().calcular_pagamento()
        return salario_base + self.comissao


## Função polimorfica
def gerar_folha_de_pagamento(funcionarios):
    custo_total = 0
    print("\n--- Folha de Pagamento ---")
    for funcionario in funcionarios:
        pagamento = funcionario.calcular_pagamento()
        custo_total += pagamento
        
        print(f"\n* {funcionario}")
        print(f"  - Pagamento do Mês: R${pagamento:.2f}")

    print("\n----------------------------------")
    print(f"Custo Total da Empresa: R${custo_total:.2f}")


## Instancias
func_mensal = FuncionarioMensal(nome="Vinicius", id_funcionario=101, salario_mensal=3000)
func_horista = FuncionarioHorista(nome="Esther", id_funcionario=102, horas_trabalhadas=160, valor_hora=20 )
# CORREÇÃO: Adicionado o salário mensal base para o funcionário comissionado
func_comissionado = FuncionarioComissionado(nome="Jean", id_funcionario=103, salario_mensal=2500, comissao=500)

lista_func = [func_mensal, func_horista, func_comissionado]

gerar_folha_de_pagamento(lista_func)