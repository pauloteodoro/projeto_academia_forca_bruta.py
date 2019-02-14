from datetime import datetime
now = datetime.now()
import random 
import xlwt
import os   
clear = lambda:os.system('clear')


def cadastro_pessoas () :                                                       #funcao para cadastro de pessoas
    clear ();
     
    continuar_cadastro = 0
    numero_alunos = 1

    wb = xlwt.Workbook()                                                                 # definindo planilha
    ws = wb.add_sheet('Controle academia FB')                                             # nomeando planilha 
    titles = ['Matricula','Nome','Telefone','Endereço','Numero','Bairro','CEP','CPF','Peso','Altura']       # titulos colunas

    
    for i in range(len(titles)):                                                      # escrever titulos das colunas

        ws.write(0, i, titles[i])

    while (continuar_cadastro != 1):

        print ("           Acadêmia Força Bruta    {}/{:0>2}/{}      {}:{} ".format(now.day,now.month,now.year,now.hour,now.minute))
        print("_______________________________________________________________________________")
        matricula_aluno = round(random.randrange(1,3000))                           # gerando numero aleatorio p/ matricula aluno
        nome_aluno = str(input(" Nome  : "))
        telefone_aluno = str(input(" Telefone  : "))                             # entrada telefone aluno
        endereco_aluno = str(input(" Endereco  : "))                              # entrada endereço aluno 
        numero_endereco_aluno = int (input(" Numero : "))                           # entrada numero da casa
        bairro_aluno = str (input(" Bairro : "))                                   # entrada bairro do aluno
        cep_aluno = int (input(" CEP : "))                                         # entrada cep aluno
        cpf_aluno = int(input(" CPF  : "))                                        # entrada cpf aluno
        peso_aluno = float(input(" Peso : "))                                       # entrada peso aluno
        altura_aluno = float(input(" Altura  : "))                                  # entrada altura aluno
        numero_alunos = numero_alunos +1
        clear()
        print("_______________________________________________________________________________")
        print(" (1) -  Enncerrar cadastramento ")
        print(" (2) -  Novo cadastro")
        continuar_cadastro = int (input(" : "))


        cadastro = [matricula_aluno,nome_aluno,telefone_aluno,endereco_aluno,numero_endereco_aluno,bairro_aluno,cep_aluno,cpf_aluno,peso_aluno,altura_aluno]

        for j in range (len(cadastro)):                                    # faz um lop para percorrer todo os itens do cadastro
        
            ws.write(numero_alunos, j, cadastro[j])                        #escreve na linha(linha,coluna, valor a escrever)

        clear()
  


     ##imc = (peso_aluno/(altura_aluno*altura_aluno))
     ##print(" IMC : {} matriula {} ".format(imc,matricula_aluno))  

     
    wb.save('Controle Academia FB.xls')                                    # Salvando arquivo



                                    


if (__name__ == "__main__"):
    cadastro_pessoas()




