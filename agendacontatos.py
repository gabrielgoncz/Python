agenda = []

def validar_texto(mensagem):
    """Garante que o campo não fique vazio ou apenas com espaços."""
    while True:
        entrada = input(mensagem).strip()
        if entrada:
            return entrada
        print("Campo não pode ficar em branco. Digite novamente: ")

def validar_telefone():
    """Garante que o telefone tenha 10 ou 11 dígitos numéricos."""
    while True:
        tel = input("Telefone (Com DDD, apenas números): ").strip()
        if (len(tel) == 10 or len(tel) == 11) and tel.isdigit():
            return tel
        print("Telefone inválido! Digite novamente (Ex: 11988887777).\n")

def buscar_email(email):
    """Retorna o índice do contato se o e-mail existir, ou -1 se não existir."""
    for i, contato in enumerate(agenda):
        if contato["email"] == email:
            return i
    return -1

def cadastrar():
    print("\n---- CADASTRAR CONTATO ----")
    nome = validar_texto("Nome: ")
    telefone = validar_telefone()
    email = validar_texto("Email: ")

    if buscar_email(email) != -1:
        print("Erro: Email já cadastrado.")
        return

    endereco = validar_texto("Endereco: ")

    novo_contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "endereco": endereco
    }

    agenda.append(novo_contato)
    print("Contato cadastrado com sucesso.")

def editar():
    print("\n---- EDITAR CONTATO ----")
    email = validar_texto("Email do contato a editar: ")

    i = buscar_email(email)
    if i == -1:
        print("Contato não encontrado.")
        return

    agenda[i]["nome"] = validar_texto("Novo nome: ")
    agenda[i]["telefone"] = validar_telefone()
    agenda[i]["email"] = validar_texto("Novo email: ")
    agenda[i]["endereco"] = validar_texto("Novo endereço: ")  

    print("Conta atualizada.")

def excluir():
    print("\n---- EXCLUIR CONTATO ----")
    email = validar_texto("Email do contato a excluir: ")

    i = buscar_email(email)
    if i == -1:
        print("Contato não encontrado.")
        return

    contato = agenda[i]
    print(f"Contato encontrado:\nNome: {contato['nome']}\nTelefone: {contato['telefone']}\nEmail: {contato['email']}\nEndereco: {contato['endereco']}")

    confirmacao = input("\nTem certeza que deseja excluir este contato? (S/N): ").strip().upper()

    if confirmacao != 'S':
        print("Exclusão cancelada.")
        return

    # Remove o contato correto usando o índice i encontrado
    agenda.pop(i)
    print("Contato excluído.")

def buscar():
    print("\n---- BUSCAR CONTATO ----")
    termo = validar_texto("Digite nome, telefone ou email: ")
    achou = False

    for contato in agenda:
        if termo in (contato["nome"], contato["telefone"], contato["email"]):
            print(f"\nNome: {contato['nome']}\nTelefone: {contato['telefone']}\nEmail: {contato['email']}\nEndereco: {contato['endereco']}")
            achou = True
            
    if not achou:
        print("Nenhum contato encontrado.")

def listar():
    if not agenda:
        print("Nenhum contato cadastrado.")
        return

    # Ordena a agenda diretamente pelo campo 'nome'
    agenda.sort(key=lambda x: x["nome"])

    print("\n--- Lista de Contatos ---")
    for i, contato in enumerate(agenda, 1):
        print(f"\n{i}. Nome: {contato['nome']}\nTelefone: {contato['telefone']}\nEmail: {contato['email']}\nEndereco: {contato['endereco']}")

def main():
    while True:
        print("\n------ AGENDA DE CONTATOS  -  SEJA BEM-VINDO ------")
        print("1 - Cadastrar Contato")
        print("2 - Editar Contato")
        print("3 - Excluir Contato")
        print("4 - Buscar Contato")
        print("5 - Listar Contatos")
        print("0 - Sair")

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            editar()
        elif opcao == "3":
            excluir()
        elif opcao == "4":
            buscar()
        elif opcao == "5":
            listar()
        elif opcao == "0":
            print("Programa encerrado. Até logo!")
            break
        else:
            print("Opção inválida!")

# Executa o programa principal corretamente
if __name__ == "__main__":
    main()
