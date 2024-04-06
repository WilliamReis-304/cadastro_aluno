from funcoes import *
info = ["1","2","3","4","5"]

escolha = {
    "1":"Adicionar Aluno",
    "2":"Ver a lista de cadastro",
    "3":"Atualizar cadastro de Aluno",
    "4":"Remover Aluno",
    "5":"Encerrar o Programa"
}
reiniciar = True

#Codigo para escolher as opções --------------------
while reiniciar == True:
    print("\nEscolha uma das opções:\n")
    resposta = input(f"1 - {escolha['1']}\n2 - {escolha['2']}\n3 - {escolha['3']}\n4 - {escolha['4']}\n5 - {escolha['5']}\n")
#Codigo para adicionar cadastro --------------------  
    if resposta == "1":
        nome = input("Digite o nome do aluno:\n")
        matricula = input("Digite a matricula do aluno:\n")
        AdicionarAluno(matricula,nome)
        reiniciar = loop()
#Codigo para visualizar a lista de cadastro --------    
    elif resposta == "2":
        VisualizarAlunos()
        reiniciar = loop()
#Codigo para atualizar a lista de cadastro ---------    
    elif resposta == "3":
        AtualizarAluno()
        reiniciar = loop()
#Codigo para remover item da lista de cadastro -----    
    elif resposta == "4":
        RemoverAlunos()
        reiniciar = loop()
#Codigo para sair do programa ----------------------    
    elif resposta == "5":
        break
print("Volte sempre!")