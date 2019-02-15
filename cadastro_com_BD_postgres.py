import psycopg2

import sys
from datetime import datetime                                       # para trabalhar com datas
now = datetime.now()
import random                                                       # para gerar numero aleatorio
import xlwt                                                         # para trabalhar com arquivos excel
import os                                                           # para usar o cler
clear = lambda:os.system('clear')

# Update connection string information obtained from the portal
host = "localhost"
user = "postgres"
dbname = "postgres"
password = "802556"
sslmode = "require"


continuar_cadastro = 0
numero_alunos = 1
wb = xlwt.Workbook()                                                        # definindo planilha
ws = wb.add_sheet('Controle academia FB')                                   # nomeando planilha 

# fazendo conexação banco de dados
conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string) 
print ("Conexão estabelecida")

cursor = conn.cursor()


cursor.execute("DROP TABLE IF EXISTS bd_cadastro;")
print ("Finished dropping table (if existed)")


# criando tabela com as colunas necessarias com repectivo nomes de coluna
cursor.execute("""CREATE TABLE bd_cadastro 
    (
    matricula_aluno serial PRIMARY KEY ,
    nome_aluno VARCHAR(50),
    telefone_aluno INTEGER ,
    endereco_aluno VARCHAR(50),
    numeroendereco_aluno INTEGER,
    bairro_aluno VARCHAR(15),
    cep_aluno VARCHAR(9),
    cpf_aluno VARCHAR(11),
    peso_aluno INTEGER,
    altura_aluno INTEGER);"""
    )   




titles = ['Matricula','Nome','Telefone','Endereço','Numero','Bairro','CEP','CPF','Peso','Altura']       # titulos colunas

    
for i in range(len(titles)):                                                # escrever titulos das colunas
    ws.write(0, i, titles[i])

while (continuar_cadastro != 1):  

            print ("           Acadêmia Força Bruta    {}/{:0>2}/{}      {}:{} ".format(now.day,now.month,now.year,now.hour,now.minute))
            print("_______________________________________________________________________________")
            matricula_aluno = round(random.randrange(1,3000))                        # gerando numero aleatorio p/ matricula aluno
            nome_aluno = str(input(" Nome  : "))
            telefone_aluno = str(input(" Telefone  : "))                             # entrada telefone aluno
            endereco_aluno = str(input(" Endereco  : "))                             # entrada endereço aluno 
            numero_endereco_aluno = int (input(" Numero : "))                        # entrada numero da casa
            bairro_aluno = str (input(" Bairro : "))                                 # entrada bairro do aluno
            cep_aluno = int (input(" CEP : "))                                       # entrada cep aluno
            cpf_aluno = int(input(" CPF  : "))                                       # entrada cpf aluno
            peso_aluno = float(input(" Peso : "))                                    # entrada peso aluno
            altura_aluno = float(input(" Altura  : "))                               # entrada altura aluno
            numero_alunos = numero_alunos +1
            clear()
            print("_______________________________________________________________________________")
            print(" (1) -  Enncerrar cadastramento ")
            print(" (2) -  Novo cadastro")
            continuar_cadastro = int (input(" : "))

            

            

            cadastro = [matricula_aluno,nome_aluno,telefone_aluno,endereco_aluno,numero_endereco_aluno,bairro_aluno,cep_aluno,cpf_aluno,peso_aluno,altura_aluno]

            # Insert some data into table
            cursor.execute("""INSERT INTO bd_cadastro 
                    (
                    matricula_aluno,
                    nome_aluno,
                    telefone_aluno,
                    endereco_aluno,
                    numeroendereco_aluno,
                    bairro_aluno,
                    cep_aluno,
                    cpf_aluno,
                    peso_aluno,
                    altura_aluno                                                    
                    )VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""", (cadastro))
            
            print ("Inserted 3 rows of data")

            for j in range (len(cadastro)):                                    # faz um lop para percorrer todo os itens do cadastro
                           
                ws.write(numero_alunos, j, cadastro[j])                        #escreve na linha(linha,coluna, valor a escrever)

wb.save('Controle Academia FB.xls')                                          # Salvando arquivo






# Cleanup
conn.commit()
cursor.close()
conn.close()