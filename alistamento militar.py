import os
os.system("CLS")

def alistamento():
    print("\n---Alistamento Militar!---")
    sexo = str(input("Nos informe seu sexo, 'masculino', 'feminino': ")).lower()

    if sexo == 'masculino':
        print("Alistamento militar obrigatório, nos forneça algumas informações:")

        nome = str(input("Digite seu nome completo: "))
        nascimento = input("Data de nascimento (formato: dd/mm/aaaa): ").strip()
        cpf = int(input("Digite seu CPF: ").strip())
        rg = int(input("Digite seu RG: ").strip())
        endereco = str(input("Digite seu endereço: "))

        return {
            'nome': nome,
            'nascimento': nascimento,
            'cpf': cpf,
            'rg': rg,
            'endereco': endereco
        }

    elif sexo == 'feminino':
        print("Alistamento militar não obrigatório!")
        opcao = input("Deseja se alistar? (sim, não): ").lower()

        if opcao == 'sim':
            print("Nos forneça algumas informações:")

            nome = str(input("Digite seu nome completo: "))
            nascimento = input("Data de nascimento (formato: dd/mm/aaaa): ").strip()
            cpf = int(input("Digite seu CPF: ").strip())
            rg = int(input("Digite seu RG: ").strip())
            endereco = str(input("Digite seu endereço: "))

            return {
                'nome': nome,
                'nascimento': nascimento,
                'cpf': cpf,
                'rg': rg,
                'endereco': endereco
            }
        else:
            print("Não deseja realizar o alistamento.")

    else:
        print("Inválido! Informe seu sexo como 'masculino' ou 'feminino'.")

dados = alistamento()

if dados:
    print("\n---Cadastro realizado---")
    print(dados)
