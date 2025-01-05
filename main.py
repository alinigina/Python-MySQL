# imporatação das bibliotecas
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

# conexão com o bd mysql
engine = sqlalchemy.create_engine('mysql+pymysql://root:@127.0.0.1:3306/teste_bd_py', echo=True)

base = declarative_base()
# create table
class User(base):
    __tablename__ = 'USERS'
    ID = Column(Integer, autoincrement=True, primary_key=True)
    NOME = Column(String(20))
    SOBRENOME = Column(String(20))
    CPF = Column(String(11), unique=True)
    # telefone
    EMAIL = Column(String(100))
    IDADE = Column(Integer)

base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def press():
    press = input("Aperte qualquer tecla para seguir...")
def select():
            busca = input(str("Deseja buscar por CPF ou por Nome? "))
            if busca == "nome":
                select = int(input("Dejesa selecionar quantos usuarios? "))
                for _ in range(select):
                    nome = input(str("Nome: "))
                    sobrenome = input(str("Sobrenome: "))
                    result = session.query(User).filter_by(NOME=nome, SOBRENOME=sobrenome).first()
                    if result:
                        print(f"Usuários encontrados: ")
                        print(f"ID: {result.ID}\nNome: {result.NOME}\nSobrenome: {result.SOBRENOME}\nCPF: {result.CPF}\nEmail: {result.EMAIL}\nIdade: {result.IDADE}")
                        press()
                    else:
                        print("Usuário não foi encontrado, tente novamente")
                        break
                functions()
            elif busca == "cpf":
                cpf = input(str("CPF: "))
                result = session.query(User).filter_by(CPF=cpf).first()
                if result:
                    print("Usuário encontrado!")
                    print(f"ID: {result.ID}\nNome: {result.NOME}\nSobrenome: {result.SOBRENOME}\nCPF: {result.CPF}\nEmail: {result.EMAIL}\nIdade: {result.IDADE}")
                    press()
                    functions()
                else:    
                    print("Usuário não encontrado!")
                    select()
            else:
                print("Erro, tente novamente")
                functions()

def fun_insert():
        insert = 1
        if  insert >= 1:
            for _ in range(insert):
                nome = input(str("Nome: "))
                sobrenome = input(str("Sobrenome: "))
                cpf = input(str("CPF: "))
                # add telefone tb
                email = input(str("Email: "))
                idade = int(input("Idade: "))
                            
                novo_usuario = User(
                NOME = nome,
                SOBRENOME = sobrenome,
                CPF = cpf,
                EMAIL = email,
                IDADE = idade,
                )
                confirm =input(str("Tem certeza que deseja adicionar esse usuário? \nSim ou Não: "))
                if confirm == "sim":
                    session.add(novo_usuario)
                    session.commit()
                    # Verifique se o usuário foi adicionado com sucesso
                    result = session.query(User).filter_by(NOME=nome, SOBRENOME=sobrenome).first()
                    if result:
                        print(f"ID: {result.ID}\nNome: {result.NOME}\nSobrenome: {result.SOBRENOME}\nCPF: {result.CPF}\nEmail: {result.EMAIL}\nIdade: {result.IDADE}")
                        print("Usuário adicionado com sucesso!")
                        retorn = input(str("Dejesa continuar os registros? \nSim ou Não: "))
                        if retorn == "sim":
                            fun_insert()
                        else:
                            functions()
                    else:
                        print("Erro ao adicionar usuário, tente novamente")
                        fun_insert()
                else:
                    print("Usuário não adicionado")
                    fun_insert()
def update():
    tamanho_max = 11
    while True:
        update = 1
        for _ in range(update):
            cpf = input(str(f"Digite o CPF do usuário que deseja atualizar ou 'exit' para sair:"))
        if len(cpf) == tamanho_max:
            result = session.query(User).filter_by(CPF=cpf).first()
            if result:
                print("Usuário encontrado!")
                print(f"ID: {result.ID}\nNome: {result.NOME}\nSobrenome: {result.SOBRENOME}\nCPF: {result.CPF}\nEmail: {result.EMAIL}\nIdade: {result.IDADE}")
                type = input(str("Digite qual o dado do usuário que dejesa alterar: "))
                if type == "nome":
                    nome = input(str("Nome: "))
                    result.NOME = nome
                    print("Nome alterado com sucesso!")
                    session.commit()
                    press()
                    update()
                elif type == "sobrenome":
                    sobrenome = input(str("Sobrenome: "))
                    result.SOBRENOME = sobrenome
                    print("Sobrenome alterado com sucesso!")
                    session.commit()
                    press()
                    update()
                elif type == "cpf":
                    cpf == input(str("CPF:"))
                    result.CPF = cpf
                    print("CPF alterado com sucesso!")
                    session.commit()
                    press()
                    update()
                elif type == "email":
                    email = input(str("Email: "))
                    result.EMAIL = email
                    print("Email alterado com sucesso!")
                    session.commit()
                    press()
                    update()
                elif type == "idade":
                    idade = input(str("Idade: "))
                    result.IDADE = idade
                    print("Idade alterada com sucesso!")
                    session.commit()
                    press()
                    update()
                else:
                    print("Usuário nao encontrado!")
                    update()
        elif cpf == "exit":
            functions()
        else:
            print(f"Erro: você digitou mais de {tamanho_max} caracteres ou o CPF digitado não foi encontrado.")
    
def functions():
    commands = input(str("Oque deseja fazer? "))
    # insert
    if commands == "insert":
        fun_insert()
    # update
    elif commands == "update":
        update()
    # select
    elif commands == "select":
        select()
    # exit
    elif commands == "sair":
        exit()
functions()