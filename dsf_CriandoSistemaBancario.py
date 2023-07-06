# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 23:40:37 2023

@author: Gabriel Louzada
"""

saldo = 2000
limite_qtdsaque = 3
limite_valsaque = 500
extrato = ''

print(" Banco DIO ".center(23, '='))
print("")
print("Olá, usuário! Seja bem-vindo(a) ao Banco DIO.")

while True:
    print(f'''
Seu saldo atual é de R${saldo:.2f}.
Por favor, digite o número da operação que você deseja realizar.

====================
[1] - Depositar
[2] - Sacar
[3] - Consultar extrato
====================
        ''')
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        print("Qual valor você deseja depositar?")
        deposito = int(input('Digite o valor em números: '))
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito de R${deposito:.2f} \n"
            print(f"O valor de R${deposito:.2f} foi depositado em sua conta.")
        else:
            print("Infelizmente o valor digitado não pôde ser computado.")
            continue
    elif opcao == 2:
        if limite_qtdsaque > 0:
            print(f'''
Você ainda tem {limite_qtdsaque} saque(s) disponível(s) hoje.
Lembre-se que o limite por saque é de R${limite_valsaque:.2f}!
Por favor, digite quanto deseja sacar.
              ''')
            saque = int(input('Digite o valor em números: '))
            if 0 < saque < saldo:
                if saque <= limite_valsaque:
                    saldo -= saque
                    extrato += f"Saque de R${saque:.2f} \n"
                    limite_qtdsaque -= 1
                    print(f"O valor de R${saque:.2f} foi sacado da sua conta.")
                else:
                    print("O valor digitado é maior que o limite permitido.")
                    continue
            elif 0 < saldo < saque:
                print("O valor digitado é maior que o seu saldo.")
                continue
            else:
                print("Infelizmente o valor digitado não pôde ser computado.")
                continue
        else:
            print("Você atingiu o limite de saques para hoje.")
            continue
    elif opcao == 3:
        print(extrato)
        continue
    else:        
        break