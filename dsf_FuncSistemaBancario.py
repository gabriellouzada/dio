# -*- coding: utf-8 -*-
"""
Created on Fri Jul 7 17:21:00 2023

@author: Gabriel Louzada
"""
# Inserir um try/except no codigo principal para usar o continue.

def novoUsuario(df, /):
    print("=" * 50)
    nome = input("Por favor, digite o seu nome completo: ").title()
    cpf = int(input("Por favor, digite o seu CPF (somente números): "))
    nascimento = input("Por favor, digite a sua data de nascimento (DD/MM/AAA): ")
    print('''Por favor, digite o seu endereço.
Siga o exemplo: Nome da rua, número - bairro - cidade/UF:''')
    endereco = input()
    if df.get(cpf):
        print(f'O CPF {cpf} já foi cadastrado.')
        return KeyError
    else:
        df[cpf] = {'Nome': nome, 'Data_de_nascimento': nascimento, 'Endereço': endereco}
        print("")
        print(f'Parabéns, {nome}! Seu cadastro foi feito com sucesso.')
        print("=" * 50)

def novaConta(dfUsuario, dfConta):
    print("=" * 50)
    cpf = int(input("Por favor, digite o seu CPF (somente números): "))
    print("")
    print(f"Olá {dfUsuario.get(cpf)['Nome']}!")
    saldo = int(input("Por favor, digite o seu saldo inicial (somente números): "))
    conta = len(dfConta)+1
    dfConta[conta] = {'CPF': cpf, 'saldo': saldo, 'limite_de_saques': 3, 'valor_limite_saque': 500}
    print("=" * 50)
    print(f'''
Obrigado por criar a sua conta conosco!
Anote os seus Conta:
Titular: {dfUsuario.get(cpf)['Nome']}
Conta: {conta}
Agência: 0001
          ''')
    print("=" * 50)

def login(dfUsuario, dfConta):
    print("=" * 50)
    conta = int(input("Por favor, digite a sua conta: "))
    if conta in dfConta.keys():
        cpf = int(input("Por favor, digite o seu CPF: "))
        if cpf in dfConta[conta].values():
            print("=" * 50)
            print(f"Seja bem-vindo(a), {dfUsuario.get(cpf)['Nome']}!")
            return [dfConta[conta]['saldo'], dfConta[conta]['limite_de_saques'], dfConta[conta]['valor_limite_saque']]
        else:
            print("Você errou o seu CPF. Tente novamente.")
            return KeyError
    else:
        print("A conta solicitada não existe. Tente novamente.")
        return KeyError

def depositar(Conta, listaExtrato, /):
    print("\nQual valor você deseja depositar?")
    deposito = int(input('Digite o valor em números: '))
    if deposito > 0:
        Conta[0] += deposito
        print(f"\nO valor de R${deposito:.2f} foi depositado em sua conta.")
        listaExtrato += addex(listaExtrato, depósito=deposito)
        return Conta, listaExtrato
    else:
        print("Infelizmente o valor digitado não pôde ser computado.")
        return KeyError

def sacar(*, Conta, listaExtrato):
    if Conta[1] > 0:
        print(f'''
Você ainda tem {Conta[1]} saque(s) disponível(s) hoje.
Lembre-se que o limite por saque é de R${Conta[2]:.2f}!
Por favor, digite quanto deseja sacar.
            ''')
        saque = int(input('Digite o valor em números: '))
        if 0 < saque < Conta[0]:
            if saque <= Conta[2]:
                Conta[0] -= saque
                listaExtrato += addex(listaExtrato, saque=saque)
                Conta[1] -= 1
                print(f"\nO valor de R${saque:.2f} foi sacado da sua conta.")
                return Conta, listaExtrato
            else:
                print("O valor digitado é maior que o limite permitido.")
                return KeyError
        elif 0 < Conta[0] < saque:
            print("O valor digitado é maior que o seu saldo.")
            return KeyError
        else:
            print("Infelizmente o valor digitado não pôde ser computado.")
            return KeyError   
    else:
        print("Você atingiu o limite de saques para hoje.")
        return KeyError   

def addex(varExtrato, /, **kwargs):
    varExtrato = '\n'.join(f'- {tipo.title()} de R${valor:.2f}\n' for tipo, valor in kwargs.items())
    return varExtrato