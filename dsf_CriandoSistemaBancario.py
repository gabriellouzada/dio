# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 23:40:37 2023

@author: Gabriel Louzada
"""
import dsf_FuncSistemaBancario as fsb

usuarios = {}
contas = {}
extrato = ''

print(" Banco DIO ".center(23, '='))

while True:
    print(f'''
Para utilizar o nosso sistema, por favor, selecione uma das opções abaixo:

=========================
[U] - Cadastrar usuário
[C] - Cadastrar conta
[L] - Logar na conta
=========================
''')

    opcao = input("Digite a opção desejada: ").upper()
    if opcao == 'U':
        try:
            fsb.novoUsuario(usuarios)
        except:
            continue
    elif opcao == 'C':
        try:
            fsb.novaConta(usuarios, contas)
        except:
            print("Este CPF não existe no nosso banco de dados. Por favor, cadastre o usuário.")
            continue
    elif opcao == 'L':
        try:
            dados = fsb.login(usuarios, contas)
            while True:
                print(f'''
Seu saldo atual é de R${dados[0]:.2f}.
Por favor, digite o número da operação que você deseja realizar.

=========================
[1] - Depositar
[2] - Sacar
[3] - Consultar extrato
=========================
                ''')
                opera = int(input("Digite a opção desejada: "))
                if opera == 1:
                    try:
                        dados, extrato = fsb.depositar(dados, extrato)
                    except:
                        continue
                elif opera == 2:
                    try:
                        dados, extrato = fsb.sacar(Conta=dados, listaExtrato=extrato)
                    except:
                        continue
                elif opera == 3:
                    print("")
                    print(extrato)
                    continue
                else:
                    print("Você foi deslogado do sistema.")        
                    break
        except:
            continue
    else:
        print("Obrigado por usar o Banco DIO. Até mais!")
        break