from dados import *

def AdicionarAluno(a,b):
    if a in cadastro.keys():
        print("Matricula ja cadastrada.\n")
    else:
        cadastro[a] = b
        print(f"Aluno cadastrado com sucesso!\n")


def VisualizarAlunos():
    if len(cadastro) == 0:
        print("Nenhum aluno cadastrado.\n")
    else:
        print(cadastro)



def AtualizarAluno():
    if len(cadastro) == 0:
        print("Nenhum aluno cadastrado.\n")
    else:
        busca = input("Digite a matricula que deseja atualizar:\n")
        if busca in cadastro.keys():
            cadastro.pop(busca)
            nome = input("Digite o nome do Aluno:\n")
            matricula = input("Digite a matricula do Aluno:\n")
            AdicionarAluno(matricula,nome)
            print("Cadastro de aluno modificado:\n",cadastro)
        else:
            print("Aluno não encontrado.\n")


    
def RemoverAlunos():
    if len(cadastro) == 0:
        print("Nenhum aluno cadastrado.\n")
    else:
        busca = input("Digite a matricula do aluno que deseja remover:\n")
        if busca in cadastro.keys():
            cadastro.pop(busca)
            print("Aluno removido:\n")
            if len(cadastro) == 0:
                print("Nenhum aluno cadastrado.\n")
            else:
                print(cadastro)
        else:
            print("Aluno não encontrado\n")



def loop():
    decisao = input("Há mais algo que deseja?(S/N)\n").upper()
    while True:
        if decisao == "S":
            return True
        elif decisao == "N":
            return False
        else:
            decisao = input("Escolha uma opção válida! S ou N\n").upper()