def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! Valor inválido.")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Saldo insuficiente.")

    elif excedeu_limite:
        print("Operação falhou! Valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Limite de saques atingido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! Valor inválido.")

    return saldo, extrato, numero_saques


def mostrar_extrato(saldo, /, *, extrato):
    print("\n========== EXTRATO ==========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("=============================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")

    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Erro: Já existe um usuário com esse CPF.")
            return

    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    endereco = input("Endereço (logradouro, Nº - bairro - cidade/UF): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("Usuário criado com sucesso!")


def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")

    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            conta = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
            contas.append(conta)
            print("Conta criada com sucesso!")
            return

    print("Erro: Usuário não encontrado. Cadastre o usuário primeiro.")


def listar_contas(contas):
    for conta in contas:
        usuario = conta["usuario"]["nome"]
        print(f"Agência: {conta['agencia']}  | Conta: {conta['numero_conta']}  | Titular: {usuario}")


# Programa principal
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário
[nc] Nova Conta
[lc] Listar Contas
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

usuarios = []
contas = []
AGENCIA = "0001"

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Valor do saque: "))
        saldo, extrato, numero_saques = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES
        )

    elif opcao == "e":
        mostrar_extrato(saldo, extrato=extrato)

    elif opcao == "nu":
        criar_usuario(usuarios)

    elif opcao == "nc":
        numero_conta = len(contas) + 1
        criar_conta(AGENCIA, numero_conta, usuarios, contas)

    elif opcao == "lc":
        listar_contas(contas)

    elif opcao == "q":
        print("Saindo do sistema... Até mais!")
        break

    else:
        print("Opção inválida! Tente novamente.")
