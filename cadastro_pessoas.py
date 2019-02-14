from datetime import datetime
now = datetime.now()


def cadastro_pessoas () :                                                       #funcao para cadastro de pessoas

    print ("Acadêmia Força Bruta    {}/{}/{}      {}:{} ".format(now.day,now.month,now.year,now.hour,now.minute)) 
    nome_aluno = str(input(" Nome  : "))                                          #  entrada nome aluno
    telefone_aluno = str(input(" telefone  : "))  

    file = str
    f = open("Cadastro Academia força Bruta.txt", "a")
    f.write("Nome : %s - Telefone: %s\n"%(nome_aluno,telefone_aluno))
    f.close

    f = file("Cadastro Academia força Bruta.txt")




if(__name__ == "__main__"):    
    cadastro_pessoas()
