menu = """

[n] Novo Cliente
[l] Listar Clientes
[c] Criar Conta

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"
id_conta = 1

clientes = []
contas = []

def criar_usuario(cpf, nome, dt_nasc, rua, bairro, cidade, uf):
    clientes.append({
            cpf: {
                "nome": nome,
                "dt_nascimento": dt_nasc,
                "endereco": {
                    "rua": rua,
                    "bairro": bairro,
                    "cidade": cidade,
                    "uf": uf            
                }
                
            }
        }
    )

def criar_conta(cpf):
    print(len(clientes))
    global id_conta
    if len(clientes) > 0:
        for item in clientes:
            if item.get(cpf):
                print(item.get(cpf))
                contas.append([AGENCIA, id_conta, cpf])
                id_conta += 1
                print(contas)
                break           
    else:
        print("Nao ha clientes cadastrados")

    

def listar_usuario(clientes): 
    #print(len(clientes))
    if len(clientes) > 0:
        for item in clientes:
            print(item)
    else:
        print("Não há clientes para listar")

def saque(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
    return saldo, extrato
    pass

def deposito(saldo, valor, extrato, /):
    return saldo, extrato
    pass

def extrato(saldo,/,*,extrato):
    pass

while True:

    opcao = input(menu)

    if opcao == "n":
        cpf = input("CPF: ")
        nome = input("Nome: ")
        dt_nasc = input("Nascimento: ")
        rua = input("Rua: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        uf = input("Estado: ")
        
        criar_usuario(cpf, nome, dt_nasc, rua, bairro, cidade, uf)
    
        
    elif opcao == "l":
        listar_usuario(clientes)
    
    elif opcao == "c":
        cpf = input("Digite o CPF do cliente: ")
        criar_conta(cpf)
    
    elif opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")